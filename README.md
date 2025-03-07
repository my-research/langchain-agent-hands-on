# LangChain 을 활용한 Agent 구현 Hands-on

jupyter notebook 을 이용하여 간단한 agent 를 생성하고 실행하는 실습 예제

# 시나리오

해당 예제 시나리오에서는 supervisor 가 있다고 가정하고 2개의 agent 만 다룬다.

### 배치 등록

- `매일 아침 10시에 우유 사줘` 라는 쿼리를 agent 에게 넘긴다.
- agent(아마도 supurvisor) 는 query 이 스케줄(배치)이 필요하다 판단하면 batch agent 을 선택한다.
- batch_agent 에서 cron 을 파싱하여 schedule 서버로 배치 생성을 요청한다
- schedule 서버의 구성은 다음과 같다 (가정)
    - 스케줄 생성 API 를 제공한다 (해당 기능은 사용자 질의와 cron 정보를 DB 에 저장한다)
    - background 에서 분마다 schedule DB 를 조회하여 실행해야 할 cron 이 존재하는지 확인한다
    - 만약 존재하면 실행한다. (실행한다면 아래 `배치 실행 당일` 로 이동한다)

### 배치 실행 당일

- 앞서 생성한 cron 정보가 실행되어야 할 시점이 도래한다면 query 를 불러온다
- `매일 아침 10시에 우유 사줘` 라는 query 에서 cron 정보를 제거한 `우유 사줘` 를 agent 에게 전달한다.
- agent 는 order tool 을 이용하여 주문을 수행한다.

# 프로젝트 구조

```text
langchain-agent-hands-on/
│── agent/                         # 에이전트 모듈
│   │── batch_agent/               # 배치 작업 관련 에이전트
│   │── order_agent/               # 주문/상품 에이전트
│   │── sample/                    # 샘플 에이전트 코드
│── docker/                        # 주문과 배치서버의 mockserver
│── .env                           # 환경 변수 설정 파일
│── .gitignore                     # Git에서 제외
```

# run local

1. agent 에서 호출할 API mockserver 실행
2. `.env` 생성 후 OpenAI key 발급 및 키 설정
3. langchain dependency 추가
4. agent 실행

### 1. mockserver 실행

```shell
cd /docker
docker-compose up -d
```

### 2. env 설정

OpenAI 에서 API key 발급 후 `.env` 파일에 넣는다.

```text
OPENAI_API_KEY=sk_******** 
```

### 3. dependency

프로젝트 내의 venv 에서 langchain 및 관련 의존성 추가

```jupyter
### 의존성 설치
# !pip install langchain
# !pip install langchain-core
# !pip install langchain-openai
# !pip install python-dotenv
```

### 4. run agent

`runner.ipynb` 파일을 생성하고 아래 코드 실행

```jupyter
from agent.batch_agent import run_agent

# 실행
result = run_agent("매일 오전 10시 30분에 신선한 우유를 쿠팡에서 주문해줘.")
print(result)
```

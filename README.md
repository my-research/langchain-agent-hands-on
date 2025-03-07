# LangChain 을 활용한 Agent 구현 Hands-on

jupyter notebook 을 이용하여 간단한 agent 를 생성하고 실행하는 실습 예제

# run local

1. `.env` 생성 후 OpenAI key 발급 및 키 설정
2. langchain dependency 추가
3. agent 실행

### 1. env 설정

OpenAI 에서 API key 발급 후 `.env` 파일에 넣는다.

```text
OPENAI_API_KEY=sk_******** 
```

### dependency

프로젝트 내의 venv 에서 langchain 및 관련 의존성 추가

```jupyter
### 의존성 설치
# !pip install langchain
# !pip install langchain-core
# !pip install langchain-openai
# !pip install python-dotenv
```

### run agent

`runner.ipynb` 파일을 생성하고 아래 코드 실행 

```jupyter
from agent.simple_agent import run_agent

# 실행
result = run_agent("`장원익` 은 몇 글자야?")
print(result)
```

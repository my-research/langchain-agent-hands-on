import requests
from langchain.tools import tool
from agent.batch_agent.util.cron_parse_util import parse_cron_from_text


@tool
def schedule_batch_job(user_input: str) -> str:
    """사용자의 자연어 요청을 받아 cron 스케줄을 생성하고 Batch API를 호출"""

    cron_expression = parse_cron_from_text(user_input)

    payload = {
        "cron_schedule": cron_expression,
        "original_query": user_input  # 사용자 입력을 그대로 저장
    }

    response = requests.post("http://localhost:1080/batch", json=payload)

    if response.status_code == 200:
        return f"✅ 배치 등록 성공: {cron_expression}"
    return f"❌ 배치 등록 실패: {response.text}"

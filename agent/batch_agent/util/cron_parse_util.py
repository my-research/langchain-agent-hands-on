import re


# TODO 이것도 가능하면 rule base 가 아니라 llm 한테 시켜야함
def parse_cron_from_text(text: str) -> str:
    """자연어 문장에서 cron 표현식을 추출하여 반환하는 함수"""

    minute = 0
    hour = 0
    day_part = "*"

    match = re.search(r"(오전|오후)?\s*(\d{1,2})시", text)
    if match:
        am_pm, hour = match.groups()
        hour = int(hour)
        if am_pm == "오후" and hour < 12:
            hour += 12  # 24시간 형식으로 변환

    if "매일" in text:
        day_part = "*"
    elif "매주" in text:
        day_part = "0"  # 매주 일요일 (기본)
    elif "매월" in text:
        day_part = "1"  # 매월 1일

    cron_expr = f"{minute} {hour} * * {day_part}"

    return cron_expr

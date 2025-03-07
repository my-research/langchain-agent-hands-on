from dotenv import load_dotenv
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser
from langchain_openai import ChatOpenAI

from agent.sample.simple_tools import tools

# API KEY 정보로드
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# 도구 바인딩
llm_with_tools = llm.bind_tools(tools)

chain1 = llm_with_tools | JsonOutputToolsParser(tools=tools)

def execute_tool_calls(tool_call_results):
    """
    도구 호출 결과를 실행하는 함수

    :param tool_call_results: 도구 호출 결과 리스트
    """
    # 도구 호출 결과 리스트를 순회합니다.
    for tool_call_result in tool_call_results:
        # 도구의 이름과 인자를 추출합니다.
        tool_name = tool_call_result["type"]  # 도구의 이름(함수명)
        tool_args = tool_call_result["args"]  # 도구에 전달되는 인자

        # 도구 이름과 일치하는 도구를 찾아 실행합니다.
        # next() 함수를 사용하여 일치하는 첫 번째 도구를 찾습니다.
        matching_tool = next((tool for tool in tools if tool.name == tool_name), None)

        if matching_tool:
            result = matching_tool.invoke(tool_args)
            # 실행 결과를 출력합니다.
            print(f"[실행도구] {tool_name} [Argument] {tool_args}\n[실행결과] {result}")
        else:
            # 일치하는 도구를 찾지 못했다면 경고 메시지를 출력합니다.
            print(f"경고: {tool_name}에 해당하는 도구를 찾을 수 없습니다.")


def run_agent(input_text):
    tool_call_results = chain1.invoke(input_text)

    chain = llm_with_tools | JsonOutputToolsParser(tools=tools) | execute_tool_calls(tool_call_results)

    chain.invoke(input_text)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from tools.simple_tools import my_tools

# api key load
load_dotenv()

llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-4o-mini",
)

# Agent 프롬프트 생성
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant, but don't know current events",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Agent 생성
agent = create_tool_calling_agent(llm, my_tools, prompt)

# AgentExecutor 생성
agent_executor = AgentExecutor(
    agent=agent,
    tools=my_tools,
    verbose=True,
    handle_parsing_errors=True,
)

def run_agent(input_text):
    result = agent_executor.invoke({"input": input_text})
    return result["output"]

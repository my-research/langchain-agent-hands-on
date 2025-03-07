from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from agent.order_agent.tools import get_products, place_order

load_dotenv()

llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-4o-mini",
)

my_tools = [get_products, place_order]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant that helps with product inquiries and orders."),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = create_tool_calling_agent(llm, my_tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=my_tools,
    verbose=True,
    handle_parsing_errors=True,
)

def run_agent(input_text):
    result = agent_executor.invoke({"input": input_text})
    return result["output"]

from langchain.agents import tool

@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word. And always plus 100 to the result"""
    return len(word) + 100

my_tools = [get_word_length]


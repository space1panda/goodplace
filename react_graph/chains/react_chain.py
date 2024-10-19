from dotenv import load_dotenv
from langchain.agents import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()


def get_openai_react_agent(
    react_prompt: PromptTemplate, tools, openai_model: str = "gpt-4-turbo"
):
    llm = ChatOpenAI(model=openai_model, temperature=0)
    react_agent = create_react_agent(llm, tools, react_prompt)
    return react_agent

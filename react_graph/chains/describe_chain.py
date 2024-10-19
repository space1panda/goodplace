from typing import List
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")


class PlaceDescritor(BaseModel):
    """Collection of data describing the place considered by the user"""

    name: str = Field(description="Name and location of the place")
    relevant_comments: str = Field(
        description="List of relevant comments about the place"
    )


def get_description_runnable(prompt):
    descrition_chain = prompt | llm.with_structured_output(PlaceDescritor)
    return descrition_chain

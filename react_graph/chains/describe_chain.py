from typing import List
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")


class URL(BaseModel):
    url: str = Field(description="URL of the image of the place")


class Comment(BaseModel):
    comment: str = Field(
            description="A comment regarding the place, which is relevant to the user's query")


class PlaceDescritor(BaseModel):
    """Collection of data describing the place considered by the user"""

    name: str = Field(
        description="Name of the place"
    )
    location: str = Field(description="Longitude and latitude of the place")
    image_urls: List[URL]
    relevant_comments: List[Comment]


pydantic_parser = PydanticOutputParser(pydantic_object=PlaceDescritor)


def get_description_runnable(prompt):
    descrition_chain = prompt | llm.bind_tools(
        tools=[TavilySearchResults(max_results=1, include_images=True)], tool_choice='tavily_search_results_json') #| pydantic_parser
    return descrition_chain

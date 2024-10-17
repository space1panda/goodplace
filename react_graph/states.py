import operator
from typing import Annotated, TypedDict, Union, Tuple, List

from langchain_core.agents import AgentAction, AgentFinish
from pydantic import BaseModel


class PlaceDescription(BaseModel):
    name: str
    location: str
    picture_urls: List[str]
    relevant_comments: List[str]


class AgentState(TypedDict):
    """
    Agent state for ReAct graph. agent_outcome will hold the type of the outcome returned by agent executor, while intermediate steps will store all Agent actions
    """

    input: str
    agent_outcome: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]
    chat_history: List[Tuple[str, str]]
    description: PlaceDescription

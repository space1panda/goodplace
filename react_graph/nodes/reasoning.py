from typing import Any, Dict, List, Tuple, Callable

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

from react_graph.chains.react_chain import get_openai_react_agent
from react_graph.states import AgentState

load_dotenv()


class ReasoningNode:
    """Logic performed by the reasoning node"""

    def __init__(self, react_prompt: ChatPromptTemplate, tools: List[Callable]):
        self._agent = get_openai_react_agent(react_prompt=react_prompt, tools=tools)

    def __call__(self, state: AgentState) -> Dict[str, Any]:
        agent_outcome = self._agent.invoke(state)
        return {"agent_outcome": agent_outcome}

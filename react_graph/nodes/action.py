from typing import Any, Dict, List, Tuple
from langgraph.prebuilt.tool_executor import ToolExecutor
from react_graph.states import AgentState


class ActionNode:
    """Logic performed by the action node"""
    def __init__(self, tools):
        self._tooler = ToolExecutor(tools)

    def __call__(self, state: AgentState) -> Dict[str, List[Tuple[Any, str]]]:
        """Logic performed by the acting node"""
        agent_action = state["agent_outcome"]
        output = self._tooler.invoke(agent_action)
        return {"intermediate_steps": [(agent_action, str(output))]}

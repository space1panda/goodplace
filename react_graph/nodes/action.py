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
        if agent_action.tool == 'tavily_search_results_json':
            query = agent_action.tool_input
            agent_action.tool_input = {
                "args": {"query": query},
                "type": "tool_call",
                "id": "foo",
                "name": "tavily",
            }
        output = self._tooler.invoke(agent_action)
        if agent_action.tool == 'tavily_search_results_json':
            try:
                images = output.artifact['images']
                if len(images) > 0:
                    res = {
                        "intermediate_steps": [(agent_action, str(output))],
                        "images": images
                        }
                else:
                    pass
            except AttributeError:
                pass
        else:
            res = {"intermediate_steps": [(agent_action, str(output))]}
        return res

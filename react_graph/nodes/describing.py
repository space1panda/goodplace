from typing import Any, Dict

from dotenv import load_dotenv
from react_graph.states import AgentState
from react_graph.chains.describe_chain import get_description_runnable
from react_graph.prompts import descriptor_prompt

load_dotenv()


class DescriptorNode:
    def __init__(self):
        self._descriptor = get_description_runnable(descriptor_prompt)

    def __call__(self, state: AgentState) -> Dict[str, Any]:
        question = state["agent_outcome"].return_values["output"]
        place_description = self._descriptor.invoke(
            {
                "input": question
            }
        )
        return {"description": place_description}

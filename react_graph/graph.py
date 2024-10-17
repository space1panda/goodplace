from dotenv import load_dotenv
from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph
from react_graph.nodes import ActionNode, ReasoningNode, DescriptorNode
from react_graph.states import AgentState
from react_graph.prompts import goodplace_react_prompt
from react_graph.tools import get_simple_tools

load_dotenv()

AGENT_REASON = "agent_reason"
AGENT_ACT = "agent_act"
DESCRIPTOR = "descriptor"


def should_continue(state: AgentState) -> str:
    """Simple conditional edge for stopping reAct loop if AgentFinish is achieved"""
    if isinstance(state["agent_outcome"], AgentFinish):
        return DESCRIPTOR
    else:
        return AGENT_ACT


# Define graph with custom schema for react pipeline


def build_react_graph(print_graph: bool = True) -> StateGraph:
    flow = StateGraph(AgentState)

    # Nodes

    tools = get_simple_tools()

    flow.set_entry_point(AGENT_REASON)
    flow.add_node(AGENT_REASON, ReasoningNode(goodplace_react_prompt, tools))
    flow.add_node(AGENT_ACT, ActionNode(tools))
    flow.add_node(DESCRIPTOR, DescriptorNode())

    # Edges
    flow.add_conditional_edges(AGENT_REASON, should_continue)

    flow.add_edge(AGENT_ACT, AGENT_REASON)
    flow.add_edge(DESCRIPTOR, END)
    app = flow.compile()
    app.get_graph().draw_mermaid_png(output_file_path="graph.png")
    return app


if __name__ == "__main__":
    print("Hello Goodplace AI")
    app = build_react_graph()
    res = app.invoke(input={"input": "Where can I dine around 6pm today?"})
    print(res["agent_outcome"].return_values["output"])

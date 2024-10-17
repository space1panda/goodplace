from typing import Any, Dict

from dotenv import load_dotenv
from react_graph.states import AgentState
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()


class DescriptorNode:
    def __init__(self):
        self._web_searcher = TavilySearchResults(
            max_results=1, include_images=True, include_raw_content=True, include_answer=True)
    
    def __call__(self, state: AgentState) -> Dict[str, Any]:
        print("--WEB-SEARCH--")
        question = state["agent_outcome"].return_values['output']
        tavily_results = self._web_searcher.invoke({"args": {'query': question}, "type": "tool_call", "id": "foo", "name": "tavily"})

        image_urls = tavily_results.artifact['images']
        return {"description": image_urls}


if __name__ == '__main__':
    web_searcher = TavilySearchResults(
            max_results=1, include_images=True, include_raw_content=True, include_answer=True)
    tavily_results = web_searcher.invoke()
    print('ok')

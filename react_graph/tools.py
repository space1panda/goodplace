import requests
from typing import Callable, List, Tuple
from datetime import datetime
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool


@tool
def current_date_and_time(input: str) -> str:
    """Function returns current date and time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def current_location_from_ip(input: str) -> Tuple[str, str]:
    """Function returns longitude and latitude of the user's device"""
    try:
        # Use ipinfo.io or ipapi.co to get location based on IP address
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        # Extract latitude and longitude
        loc = data.get("loc", "0,0").split(",")
        latitude = loc[0]
        longitude = loc[1]

        return latitude, longitude
    except requests.exceptions.RequestException as e:
        return f"Error retrieving location: {e}"


def get_simple_tools() -> List[Callable]:
    tools = [TavilySearchResults(max_results=1), current_date_and_time, current_location_from_ip]
    return tools

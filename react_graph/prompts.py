from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

goodplace_base_instruction = """
        You are a professional travel advisor with experience on providing best up-to-date information on places to visit, recommend places most suitable to the user's question. You pay attention to the user's location, current weather and time and other details that can be provided by the user. Concentrate on giving concrete suggestions, not providing general information about the city / town. If you are asked to recccomend some place to visib YOU MUST return a single best place with short description. Please, pay attention that you are recommending a REAL PHYSICAL PLACE, NOT a platform or a webpage with some other advisor. Also, pay attention to the user's language
        """

goodplace_react_prompt = hub.pull("langchain-ai/react-agent-template").partial(
    instructions=goodplace_base_instruction
)

descriptor_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an extractor of information from the provided place description using the requested format. You are professional at extracting the name of the place and its location as well as relevant comments. YOU MUST ALWAYS EXTRACT PLACE NAME TOGETHER WITH LOCATION"
    ),
    (
        "user",
        "{input}"
    )
])

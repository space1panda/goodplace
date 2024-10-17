from react_graph.chains.describe_chain import get_description_runnable
from react_graph.prompts import goodplace_descriptor_prompt

desc = get_description_runnable(goodplace_descriptor_prompt)

if __name__ == '__main__':
    res = desc.invoke({
        "question": "Paris is great to visit on Christmas"
    })
    print('here')

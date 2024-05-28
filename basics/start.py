import io
from typing import List

from PIL import Image
from langgraph.graph import MessageGraph, END
from langchain_core.messages import HumanMessage


def add_one(input: List[HumanMessage]):
    print("a",input[0].content)
    input[0].content = input[0].content + 'a'
    return input

def add_oneb(input: List[HumanMessage]):
    print("b",input[0].content)
    input[0].content = input[0].content + 'b'
    return input

def add_onec(input: List[HumanMessage]):
    print("c",input[0].content)
    input[0].content = input[0].content + 'c'
    return input

def should_continue(input: List[HumanMessage]):
    last_message = input[-1].content
    if 'p' in last_message:
        return 'branch_b'
    return 'branch_c'

graph = MessageGraph()

graph.add_node('branch_a',add_one)
graph.add_node('branch_b',add_oneb)
graph.add_node('branch_c',add_onec)


graph.add_conditional_edges(
    "branch_a",
    should_continue,
    {"branch_b":'branch_b','branch_c':'branch_c'}
)

graph.set_entry_point('branch_a')
graph.set_finish_point('branch_b')
graph.set_finish_point('branch_c')

runnable = graph.compile()

# Image.open(io.BytesIO(runnable.get_graph().draw_mermaid_png())).show()

print(runnable.invoke("p"))


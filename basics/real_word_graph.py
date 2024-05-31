import operator
import random
from typing import TypedDict, List, Annotated, Sequence

from langchain_community.chat_models import ChatOllama
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool, Tool
from langchain_experimental.llms.ollama_functions import OllamaFunctions

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    api_call_count: int = 0


@tool
def fake_weather_api(city: str) -> str:
    """Check the weather in a specified city. The API is available randomly, approximately every third call"""

    if random.randint(1, 3) == 1:
        return "Sunny,22 degree celsius"
    else:
        return "Service temporarily unavailable"

def stream_response(input:str,model):
    for _ in model.stream(input):
        print(_.content,end="",flush=True)

model = OllamaFunctions(model = "tinyllama",format= "json")
input = "who is weather in Boston?"

tools = [fake_weather_api]






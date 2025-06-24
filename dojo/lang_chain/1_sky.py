from langchain_openai import ChatOpenAI  # ✅ new import
from langchain_core.messages import HumanMessage  # ✅ new core message schema

import os

api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=api_key,
    temperature=0.3,
)

# ✅ use `.invoke()` instead of calling directly
messages = [HumanMessage(content="Write a short test for an Elixir double/1 function.")]
response = chat.invoke(messages)

print(response.content)

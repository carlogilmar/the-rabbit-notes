from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class AnswerWithJustification(BaseModel):
    answer: str
    justification: str

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
structured_llm = llm.with_structured_output(AnswerWithJustification)

print("Sending prompt...")
response = structured_llm.invoke("What weights more, a pound of bricks or a pound of feathers")
print(response.answer)
print(response.justification)

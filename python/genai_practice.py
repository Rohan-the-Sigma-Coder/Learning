import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.runnables import RunnablePassthrough

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise RuntimeError("Set HUGGINGFACEHUB_API_TOKEN in your environment")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large", 
    temperature=0.7,
    max_new_tokens=200
)

cuisine_prompt_template = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)
items_template_name = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest some menu food items for  {restaurant_name}. Return it as comma seperated list."
)

chain = (
    cuisine_prompt_template
    | llm 
    | {"restaurant_name": RunnablePassthrough()}  # Pass output to next step
    | items_template_name
    | llm
)
response = chain.invoke({"cuisine": "Indian"})
print(response)






import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise RuntimeError("Set HUGGINGFACEHUB_API_TOKEN in your environment")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",  # ✅ Supports text-generation
    temperature=0.7,
    max_new_tokens=200
)

prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

chain = prompt_template_name | llm
result = chain.invoke({"cuisine": "Indian"})
print(result)








import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise RuntimeError("Set HUGGINGFACEHUB_API_TOKEN in your environment")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
# Use a chat/text-generation supported model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # Chat-compatible model
    temperature=0.7,
    max_new_tokens=200
)

# Wrap in ChatHuggingFace for proper chat interface
chat_llm = ChatHuggingFace(llm=llm)

# Invoke with HumanMessage
response = chat_llm.invoke([HumanMessage(content="Hello")])
print(response.content)






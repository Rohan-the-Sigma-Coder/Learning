from Learning.pythonfiles.genai_course import ChatAnthropic

llm = ChatAnthropic(
    model="claude-3-5-sonnet-latest",
    anthropic_api_key="YOUR_ANTHROPIC_KEY"
)

print(llm.invoke("Hello"))


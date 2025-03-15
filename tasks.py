# tasks.py
from crewai import Task
from agents import GPTAgent

gpt_agent = GPTAgent()

# Define a Task
query_task = Task(
    description="Answer the user's question using the OpenAI Assistant API.",
    agent=None,
    expected_output="A well-structured response from GPT.",
    callback=lambda query: gpt_agent.chat_with_assistant(str(query))  # ✅ Ensure input is always a string
)

# query_task = Task(
#     description="Answer the user's question using the OpenAI Assistant API.",
#     agent=assistant_agent,
#     expected_output="A well-structured response from GPT Assistant.",
#     callback=lambda query: gpt_agent.chat_with_assistant(query)
# )

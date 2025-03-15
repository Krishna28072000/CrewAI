# agents.py
from crewai import Agent
from config import OPENAI_API_KEY
import openai

class GPTAgent:
    def __init__(self):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)

    def chat_with_assistant(self, user_query): 
        response = self.client.chat.completions.create(
            model = "gpt-4o",
            messages=[{"role":"system","content":"You are an AI assistant. Answer concisely"},
                      {"role":"user", "content":user_query}]
        )
        return response.choices[0].message.content
    
gpt_agent = GPTAgent()


    # def chat_with_assistant(self, user_query):
    #     response = self.client.beta.threads.create_and_run(
    #         assistant_id=GPT_ASSISTANT_ID,
    #         thread={"messages": [{"role": "user", "content": user_query}]}
    #     )
    #     return response

# # Create CrewAI Agent
# assistant_agent = Agent(
#     role="AI Assistant",
#     goal="Answer user queries using OpenAI Assistant API",
#     backstory="A knowledgeable assistant trained to provide accurate information.",
#     allow_delegation=False
# )

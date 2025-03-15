# main.py
from crew import run_crew

if __name__ == "__main__":
    user_input = input("Ask a question: ")
    response = run_crew(user_input)
    print("Assistant Response:", response)
    
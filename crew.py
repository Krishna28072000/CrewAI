# crew.py
from crewai import Crew
from tasks import query_task

def run_crew(user_input):
    return query_task.callback(user_input) 

import platform
import os
from groq import Groq

def initialize_chat_model(model_choice):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    return client

def generate_command(model_choice: str, instruction: str) -> str:
    os_type = platform.system()
    shell_type = os.environ.get('SHELL') or os.environ.get('COMSPEC')

    chat = initialize_chat_model(model_choice)
    
    system_message = (
        "system",
        f"You are a helpful {os_type} assistant that generates {shell_type} commands based on user instruction. You must only output the command that can be executed in {shell_type}. Do not wrap the command in quotes",
    )

    human_message = ("human", instruction)

    chat_completion = chat.invoke([system_message, human_message])
    return chat_completion.choices[0].message.content
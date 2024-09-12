from langchain_openai import ChatOpenAI
import platform
import os

def initialize_chat_model(model_choice):
    return ChatOpenAI(model=model_choice)

def generate_command(model_choice: str, instruction: str) -> str:
    os_type = platform.system()
    shell_type = os.environ.get('SHELL') or os.environ.get('COMSPEC')

    chat = initialize_chat_model(model_choice)
    
    system_message = (
        "system",
        f"You are a helpful {os_type} assistant that generates {shell_type} commands based on user instruction. You must only output the command that can be executed in {shell_type}. Do not wrap the command in quotes",
    )

    human_message = ("human", instruction)

    response = chat.invoke([system_message, human_message])
    return response.content
import platform
import os
from groq import Groq
from config import load_command_cache, save_command_cache

def initialize_chat_model():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    return client

def generate_command(model_choice: str, instruction: str) -> str:
    os_type = platform.system()
    shell_type = os.environ.get('SHELL') or os.environ.get('COMSPEC')

    # Load command cache
    command_cache = load_command_cache()

    # Normalize instruction
    normalized_instruction = instruction.lower().strip()

    # Check if command is already cached
    if normalized_instruction in command_cache:
        return command_cache[normalized_instruction]
    
    chat = initialize_chat_model()
    chat_completion = chat.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful {os_type} assistant that generates {shell_type} commands based on user instruction. You must only output the command that can be executed in {shell_type}. Do not wrap the command in quotes",
            },
            {
                "role": "user",
                "content": instruction,
            }
        ],
        model=model_choice,
    )
    
    command = chat_completion.choices[0].message.content
    # Cache the command
    command_cache[normalized_instruction] = command
    save_command_cache(command_cache)  # Save updated command cache
    return command
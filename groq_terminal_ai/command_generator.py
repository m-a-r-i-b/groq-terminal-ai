import platform
import os
from groq import Groq
from config import load_command_cache, save_command_cache, load_instruction_history, save_instruction_history

def initialize_chat_model():
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    return client

def generate_command(model_choice: str, instruction: str, history_size: int = 3) -> str:
    os_type = platform.system()
    shell_type = os.environ.get('SHELL') or os.environ.get('COMSPEC')

    command_cache = load_command_cache()
    instruction_history = load_instruction_history()

    normalized_instruction = instruction.lower().strip()

    if normalized_instruction in command_cache:
        return command_cache[normalized_instruction]
    
    chat = initialize_chat_model()

    context = ""
    if instruction_history:
        context = "Here are the previous instruction-command pairs of user that may or may not be related to the current instruction:\n"
        for prev_instruction, prev_command in instruction_history:
            context += f"- **Instruction**: {prev_instruction}\n  **Command**: {prev_command}\n\n"

    chat_completion = chat.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful {os_type} assistant that generates {shell_type} commands based on user instruction. {context} You must only output the command that can be executed in {shell_type}. Do not wrap the command in quotes",
            },
            {
                "role": "user",
                "content": instruction,
            }
        ],
        model=model_choice,
    )
    
    command = chat_completion.choices[0].message.content
    command_cache[normalized_instruction] = command
    save_command_cache(command_cache)

    instruction_history.append((instruction, command))
    if len(instruction_history) > history_size:
        instruction_history = instruction_history[-history_size:]
    save_instruction_history(instruction_history)

    return command
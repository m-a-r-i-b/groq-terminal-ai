import sys
import pyautogui
from groq_terminal_ai.config import load_config, save_api_key, save_model
from groq_terminal_ai.models import ModelEnum
from groq_terminal_ai.utils import parse_arguments
from groq_terminal_ai.command_generator import generate_command

def main():
    args = parse_arguments()
    config = load_config()
    
    if args.groq_api_key:
        save_api_key(args.groq_api_key)
        sys.exit(0)

    if args.model:
        save_model(args.model)
        sys.exit(0)

    api_key = config.get('GROQ_API_KEY')
    if not api_key:
        print("Please set the GROQ_API_KEY with 'ai --groq-api-key <key>'.")
        sys.exit(1)

    model_choice = args.model or config.get('MODEL') or ModelEnum.LLAMA3_8B_8192.value

    if args.instruction:
        command = generate_command(model_choice, ' '.join(args.instruction))
        pyautogui.write(command)
    else:
        print("Please provide an instruction to execute.")

if __name__ == "__main__":
    main()

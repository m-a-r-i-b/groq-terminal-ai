import sys
import pyautogui
from cli_ai.config import load_config, save_api_key, save_model
from cli_ai.models import ModelEnum
from cli_ai.utils import parse_arguments
from cli_ai.command_generator import generate_command

def main():
    args = parse_arguments()
    config = load_config()
    
    if args.openai_api_key:
        save_api_key(args.openai_api_key)
        sys.exit(0)

    if args.model:
        save_model(args.model)
        sys.exit(0)

    api_key = config.get('OPENAI_API_KEY')
    if not api_key:
        print("Please set the OPENAI_API_KEY with 'ai --openai-api-key <key>'.")
        sys.exit(1)

    model_choice = args.model or config.get('MODEL') or ModelEnum.GPT_4_Omni_Mini.value

    if args.instruction:
        command = generate_command(model_choice, ' '.join(args.instruction))
        pyautogui.write(command)
    else:
        print("Please provide an instruction to execute.")

if __name__ == "__main__":
    main()

import sys
from groq_terminal_ai.config import (
    load_config, save_api_key, save_model, save_history_size, load_history_size,
    save_use_history, load_use_history
)
from groq_terminal_ai.models import ModelEnum
from groq_terminal_ai.utils import parse_arguments
from groq_terminal_ai.command_generator import generate_command

def main():
    args = parse_arguments()
    config = load_config()
    
    if args.groq_api_key:
        save_api_key(args.groq_api_key)
    if args.model:
        save_model(args.model)
    if args.use_history is not None:
        save_use_history(args.use_history)
    if args.history_size:
        save_history_size(args.history_size)
    

    # Exit if any of the above arguments were provided
    if any([args.groq_api_key, args.model, args.history_size, args.use_history is not None]):
        sys.exit(0)

    api_key = config.get('GROQ_API_KEY')
    if not api_key:
        print("Please set the GROQ_API_KEY with 'ai --groq-api-key <key>'.")
        sys.exit(1)

    model_choice = args.model or config.get('MODEL') or ModelEnum.LLAMA3_1_8B_INSTANT.value
    history_size = args.history_size if args.history_size is not None else load_history_size()
    use_history = args.use_history if args.use_history is not None else load_use_history()

    if args.instruction:
        generate_command(model_choice, ' '.join(args.instruction), history_size, use_history)
    else:
        print("Please provide an instruction to execute. or use --help for more information.")

if __name__ == "__main__":
    main()

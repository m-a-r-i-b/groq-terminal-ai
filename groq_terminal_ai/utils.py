import argparse
from groq_terminal_ai.models import ModelEnum

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate bash commands based on user input.")
    parser.add_argument('--groq-api-key', type=str, help='Set the Groq API key.')
    
    # Add model argument with validation
    parser.add_argument('--model', type=str, choices=[model.value for model in ModelEnum], 
                        help='Set the Groq model to use. Supported models: ' + ', '.join([model.value for model in ModelEnum]))
    parser.add_argument('--history-size', type=int, help='Set the default number of previous instructions to retain in history (default: 3)')
    parser.add_argument('--use-history', type=str, help='Use instruction history (default: True)')
    parser.add_argument('instruction', nargs='*', help='The instruction to execute.')
    
    args = parser.parse_args()

    # Convert use_history to boolean
    if args.use_history is not None:
        args.use_history = args.use_history.lower() == 'true'
    
    return args
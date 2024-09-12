import argparse
from terminal_ai.models import ModelEnum

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate bash commands based on user input.")
    parser.add_argument('--openai-api-key', type=str, help='Set the OpenAI API key.')
    
    # Add model argument with validation
    parser.add_argument('--model', type=str, choices=[model.value for model in ModelEnum], 
                        help='Set the OpenAI model to use. Supported models: ' + ', '.join([model.value for model in ModelEnum]))
    parser.add_argument('instruction', nargs='*', help='The instruction to execute.')
    
    return parser.parse_args()
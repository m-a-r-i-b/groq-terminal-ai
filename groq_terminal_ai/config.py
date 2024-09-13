import os
import json
import site

CONFIG_PATH = os.path.join(site.getsitepackages()[0], 'config.json')

config_cache = None

def load_config():
    global config_cache  # Use the global variable
    if config_cache:  # Check if already loaded
        return config_cache
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as config_file:
            try:
                config_cache = json.load(config_file)
            except json.JSONDecodeError:
                config_cache = {}
            if 'GROQ_API_KEY' in config_cache:
                os.environ['GROQ_API_KEY'] = config_cache['GROQ_API_KEY']
            return config_cache
    return {}

# Global variable to store the loaded configuration
config_cache = load_config()

def save_config(config):
    global config_cache  # Use the global variable
    with open(CONFIG_PATH, 'w') as config_file:
        json.dump(config, config_file)
    config_cache = config  # Update the cache

# Update all save functions to use the cached config
def save_api_key(api_key):
    config_cache['GROQ_API_KEY'] = api_key
    save_config(config_cache)
    print(f"GROQ_API_KEY saved at {CONFIG_PATH}.")

def save_model(model):
    config_cache['MODEL'] = model
    save_config(config_cache)
    # print(f"MODEL saved at {CONFIG_PATH}.")

def save_command_cache(command_cache):
    config_cache['COMMAND_CACHE'] = command_cache
    save_config(config_cache)
    # print(f"COMMAND_CACHE saved at {CONFIG_PATH}.")

def load_command_cache():
    return config_cache.get('COMMAND_CACHE', {})

def save_instruction_history(instruction_history):
    config_cache['INSTRUCTION_HISTORY'] = instruction_history
    save_config(config_cache)
    # print(f"INSTRUCTION_HISTORY saved at {CONFIG_PATH}.")

def load_instruction_history():
    return config_cache.get('INSTRUCTION_HISTORY', [])

def save_history_size(history_size):
    config_cache['HISTORY_SIZE'] = history_size
    save_config(config_cache)
    # print(f"HISTORY_SIZE saved at {CONFIG_PATH}.")

def load_history_size():
    return config_cache.get('HISTORY_SIZE', 3)  # Default to 3 if not set

def save_use_history(use_history):
    config_cache['USE_HISTORY'] = use_history
    save_config(config_cache)
    # print(f"USE_HISTORY saved at {CONFIG_PATH}. {use_history}")

def load_use_history():
    return config_cache.get('USE_HISTORY', True)  # Default to True if not set
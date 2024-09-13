import os
import json
import site

CONFIG_PATH = os.path.join(site.getsitepackages()[0], 'config.json')

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as config_file:
            config = json.load(config_file)
            if 'GROQ_API_KEY' in config:
                os.environ['GROQ_API_KEY'] = config['GROQ_API_KEY']
            return config
    return {}

def save_config(config):
    with open(CONFIG_PATH, 'w') as config_file:
        json.dump(config, config_file)

def save_api_key(api_key):
    config = load_config()
    config['GROQ_API_KEY'] = api_key
    save_config(config)
    print(f"GROQ_API_KEY saved at {CONFIG_PATH}.")

def save_model(model):
    config = load_config()
    config['MODEL'] = model
    save_config(config)
    print(f"MODEL saved at {CONFIG_PATH}.")

def save_command_cache(command_cache):
    config = load_config()
    config['COMMAND_CACHE'] = command_cache
    save_config(config)
    print(f"COMMAND_CACHE saved at {CONFIG_PATH}.")

def load_command_cache():
    config = load_config()
    return config.get('COMMAND_CACHE', {})

def save_instruction_history(instruction_history):
    config = load_config()
    config['INSTRUCTION_HISTORY'] = instruction_history
    save_config(config)
    print(f"INSTRUCTION_HISTORY saved at {CONFIG_PATH}.")

def load_instruction_history():
    config = load_config()
    return config.get('INSTRUCTION_HISTORY', [])

def save_history_size(history_size):
    config = load_config()
    config['HISTORY_SIZE'] = history_size
    save_config(config)
    print(f"HISTORY_SIZE saved at {CONFIG_PATH}.")

def load_history_size():
    config = load_config()
    return config.get('HISTORY_SIZE', 3)  # Default to 3 if not set

def save_use_history(use_history):
    config = load_config()
    config['USE_HISTORY'] = use_history
    save_config(config)
    print(f"USE_HISTORY saved at {CONFIG_PATH}. {use_history}")

def load_use_history():
    config = load_config()
    return config.get('USE_HISTORY', True)  # Default to True if not set
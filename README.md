# groq-terminal-ai



https://github.com/user-attachments/assets/a6cb57a5-a597-438c-b976-4a6fd48960af



**groq-terminal-ai** is a cross-platform CLI tool that utilizes Groq's API to intelligently generate terminal commands from natural language instructions. It supports Linux, macOS, and Windows.

## Key Features

- **AI-Powered Command Generation**: Leverages Groq's advanced language models to interpret user instructions and generate accurate terminal commands.
- **Cross-Platform Compatibility**: Seamlessly operates on Linux, macOS, and Windows operating systems.
- **Customizable Model Selection**: Offers flexibility to choose from different LLM models for tailored command generation.
- **Command History**: Maintains a history of previous instructions and commands for context-aware suggestions.
- **Efficient Caching**: Implements a command cache to quickly retrieve previously generated commands.

## Installation

Install groq-terminal-ai using pip:

```bash
pip install groq-terminal-ai
```

## Usage

Step 1. Set your Groq API key
```bash
ai --groq-api-key <your-api-key>
```

Step 2. Generate a command
```bash
ai list all png files in the current directory
```

### Optional Parameters

- Choose a specific LLM model:
  ```bash
  ai --model <model-name> (default llama-3.1-8b-instant)
  ```

- Set the history size for context-aware suggestions:
  ```bash
  ai --history-size <number> (default 3)
  ```

- Enable or disable instruction history:
  ```bash
  ai --use-history <true/false> (default true)
  ```

- For more information on available options:
  ```bash
  ai --help
  ```

## Supported Models

### Current Production Models

- **llama-3.3-70b-versatile** - Latest Llama 3.3 model with excellent reasoning capabilities
- **llama-3.1-8b-instant** - Fast and efficient model, great for quick command generation
- **gemma2-9b-it** - Google's Gemma 2 model optimized for instruction following

### Latest Advanced Models

- **meta-llama/llama-4-scout-17b-16e-instruct** - Llama 4 Scout for complex reasoning tasks
- **meta-llama/llama-4-maverick-17b-128e-instruct** - Llama 4 Maverick for multilingual tasks
- **deepseek-r1-distill-llama-70b** - Advanced reasoning model for complex problem-solving
- **deepseek-r1-distill-qwen-32b** - Efficient reasoning model with strong coding capabilities
- **qwen-2.5-32b** - Qwen 2.5 with improved coding and instruction following
- **qwen-qwq-32b** - Latest Qwen reasoning model
- **mistral-saba-24b** - Updated Mistral model

### Legacy Models (Being Deprecated)

- **llama3-70b-8192** - Will be deprecated on August 30, 2025 (use llama-3.3-70b-versatile instead)
- **llama3-8b-8192** - Will be deprecated on August 30, 2025 (use llama-3.1-8b-instant instead)

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
  ai --model <model-name> (default llama3-8b-8192)
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

- llama3-8b-8192
- gemma2-9b-it
- gemma-7b-it
- llama3-70b-8192
- llama-3.1-70b-versatile
- llama-3.1-8b-instant
- llava-v1.5-7b-4096-preview
- mixtral-8x7b-32768

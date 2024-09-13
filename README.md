# groq-terminal-ai

**groq-terminal-ai** is a CLI tool that harnesses the power of Groq's API to intelligently generate terminal commands based on natural language instructions.

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
  ai --model <model-name>
  ```

- Set the history size for context-aware suggestions:
  ```bash
  ai --history-size <number>
  ```

- Enable or disable instruction history:
  ```bash
  ai --use-history <true/false>
  ```

- For more information on available options:
  ```bash
  ai --help
```

## Supported Models

- llama3-8b-8192
- gemma2-9b-it
- llama3-70b-8192
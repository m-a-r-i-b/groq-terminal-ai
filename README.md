# groq-terminal-ai

## Description
groq-terminal-ai is a command line tool that uses Groq's API to generate terminal commands.

## Features
- Minimal setup
- Ability to choose between different LLMs from Groq


## Installation

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

(Optional) Choose a different LLM model
```bash
ai --model <model-name>
```

```bash
ai --help
```


## License
This project is licensed under the MIT License.

# cli-ai

## Description
cli-ai is a command line tool that uses OpenAI's API to generate terminal commands.

## Features
- Minimal setup
- Ability to choose between different LLMs from OpenAI


## Installation

```bash
pip install cli-ai
```

## Usage

Step 1. Set your OpenAI API key
```bash
ai --openai-api-key <your-api-key>
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

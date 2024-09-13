# groq-terminal-ai

## Description
**groq-terminal-ai** is a powerful command-line tool that leverages Groq's API to intelligently generate terminal commands based on user instructions.

## Features
- **High Performance**: Utilizes Groq's API for rapid command generation.
- **Cross-Platform Compatibility**: Works seamlessly on Linux, Windows, and Mac operating systems.
- **Minimal Setup**: Quick installation and easy configuration.
- **Customizable**: Option to select different LLM models for tailored command generation.


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

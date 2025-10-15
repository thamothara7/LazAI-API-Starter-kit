# Demo Project

## Installation
To avoid dependency conflicts and keep your environment clean, create and activate a Python virtual environment before installing any packages.

### macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows OS:
```bash
python -m venv venv
venv/Scripts/activate
```
## Install Alith Mac

```bash
python3 -m pip install alith -U
```
## Install Alith Windows

```bash
python -m pip install alith -U
```

## Start Inference Server

Before running the inference script, ensure you have an inference server running either:

1. Locally on your machine, or
2. In a Trusted Execution Environment (TEE) Cloud

The inference server must be registered with LazAI. 


## Environment Setup

Create a .env file in your project root to securely store your private keys and API keys.

Example .env file
 ```
PRIVATE_KEY=<your wallet private key>
GROQ_API_KEY=<your groq api key>
```
Important:

Never share or upload your .env file to GitHub.
Ensure .env is listed in your .gitignore file.

### For OpenAI/ChatGPT API:

```bash
export PRIVATE_KEY=<your wallet private key>
```

### To run the inference script

```bash
python inference.py
``` 
### Quick Setup Summary:

1. Create and activate a virtual environment
2. Install dependencies (alith)
3. Set up your .env file
4. Start your inference server
5. Run python inference.py

### Troubleshooting

Dependency errors: Reinstall packages inside your virtual environment
Missing .env variables: Ensure .env is in your project root and properly formatted
Server errors: Make sure your inference server is registered with LazAI and accessible
# Demo Project

## Installation

To avoid dependency conflicts and keep your environment clean, create and activate a Python virtual environment before installing any packages:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Alith

```bash
python3 -m pip install alith -U
```

## Start Inference Server

Before running the inference script, ensure you have an inference server running either:

1. Locally on your machine, or
2. In a Trusted Execution Environment (TEE) Cloud

The inference server must be registered with LazAI. 


## Set Environment Variables

### For OpenAI/ChatGPT API:

```bash
export PRIVATE_KEY=<your wallet private key>
```

### To run the inference script

```bash
python inference.py
``` 
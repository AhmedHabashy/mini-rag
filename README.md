# mini-rag

Minimal implementation of a simple rag system practicing software engineering concepts

## Requirements

- python 3.14

## installation and setup

1) Download python 3.14
2) create a new environment 
```bash
python -m venv .venv
```
3) activate environment 
```bash
source ./.venv/Scripts/activate
```

## Run fastapi server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
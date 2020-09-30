# REPRO

## Setup Python

```bash
python3.8 -m venv env
source env/bin/activate
```

## Setup Environment

```bash
export FR_ENDPOINT=https://myresource.cognitiveservices.azure.com/
export FR_KEY=mysecret
export FR_LOCAL_PATH=/path/to/file.pdf
```

## Run

```bash
python ./main.py
```

Observe HTTP logging is output twice: once unredacted and once redacted.
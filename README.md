# Flask Hello World

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000/` to see `Hello World`.

## Run with Docker

```bash
docker build -t flask-hello .
docker run --rm -p 5000:5000 flask-hello
```

Then open `http://localhost:5000/`.


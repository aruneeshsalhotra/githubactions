"""Minimal Flask app that returns 'Hello World'."""

import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello_world():
    """Return a friendly greeting."""
    return "Hello World"


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "").lower() in {"1", "true", "yes", "on"}
    app.run(host=host, port=port, debug=debug)

#!/usr/bin/env python3
"""Basic setup: Task 0"""

from flask import Flask, render_template

app = Flask(__name___)


@app.route("/")
def index():
    """this is the default route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)

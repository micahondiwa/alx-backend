#!/usr/bin/env python3

"""The flask application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.rout("/")
def index():
    return render_template("0-index.html")


if __name__ == "__manin__":
    app.run(debug=True)

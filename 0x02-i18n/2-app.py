#!/usr/bin/env python3
"""Task 2: get locale from request"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """the Config class"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """retrieves and returns the locale

    Returns:
    str: best match"""

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """default route for the app

    Returns:
    html: home page
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)

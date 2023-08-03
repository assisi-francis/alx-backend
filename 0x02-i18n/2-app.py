#!/usr/bin/env python3
"""
the Babel Flask extension
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

# Config class with available languages


class Config:
    """
    config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate Babel object and configure it

app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    return template
    """
    return render_template('2-index.html')


def get_locale():
    """
    Get the best-matching language based on request.accept_languages
    @babel.localeselector
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)

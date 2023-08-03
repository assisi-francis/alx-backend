#!/usr/bin/env python3
"""
the Babel Flask extension
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

# Config class with available languages


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Instantiate Babel object and configure it


babel = Babel(app)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

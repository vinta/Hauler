# coding: utf-8

import os

from flask import Flask, render_template, request

from raven.contrib.flask import Sentry

from api.api import api


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.config.from_object(os.environ.get('HAULER_CONFIG_PATH', 'config.ProductionConfig'))

# Sentry will read DSN from environment under the SENTRY_DSN key
sentry = Sentry(app)


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/')
@app.route('/demo/')
def demo():
    return render_template('demo.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

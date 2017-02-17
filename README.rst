Installation
============

::

    pip install Flask-kinesis

Configuration
=============

Takes just one configuration setting, of ``EVENT_TAG_PREFIX``, which is prepended
to the tag of all outgoing events.

Usage
=====

::

    from flask import Flask, g
    from flask_kinesis import kinesis


    app = Flask(__name__)
    events = kinesis(app)

    @app.before_request
    def before_request():
        g.events = events

    # ...

    @app.route('/')
    def index():
        g.events.event({'foo': 'bar'})

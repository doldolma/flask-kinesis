Installation
============

::

    pip install Flask-kinesis

Usage
=====

::

    from flask import Flask, g
    from flask_kinesis import kinesis

    # credentials information can be omitted

    app = Flask(__name__)
    kinesis(app,
            aws_access_key_id= "",
            aws_access_secret_key= "",
            region_name= "",
            StreamName="")

    # ...

    @app.route('/')
    def index():
        g.events.event({'foo': 'bar'})

"""
Flask-Kinesis
-------------

With this library, you can simply record events from the flask application to aws kinesis
"""

from distutils.core import setup

setup(
    name="Flask-kinesis",
    version="0.1.6",
    py_modules=["flask_kinesis"],
    author="doyoung",
    author_email="iidd58" "@" "gmail.com",
    url="https://github.com/iidd0101/flask-kinesis",
    license="MIT",
    description="Flask plugin for aws kinesis stream",
    long_description=__doc__,
    platforms="any",
    install_requires=[
        "Flask",
        "boto3"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Flask",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Natural Language :: Korean",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

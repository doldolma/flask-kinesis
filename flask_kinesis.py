# coding: utf8
import boto3
import json
from boto3.session import Session
from Queue import Queue, Empty
from flask import g


class kinesis(object):

    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app)
            app.before_request(self.before_request)
            app.after_request(self.send_events)

            self.queue = Queue()
            credentials = Session().get_credentials()
            try:
                self.kinesis = boto3.client(
                    'kinesis',
                    aws_access_key_id=kwargs.get(
                        "aws_access_key_id",
                        credentials.access_key
                    ),
                    aws_secret_access_key=kwargs.get('aws_secret_access_key',
                                                     credentials.secret_key),
                    region_name=kwargs.get("region_name", Session().region_name)
                )
                self.StreamName = kwargs['StreamName']
            except:
                raise TypeError("aws_access_key_id, aws_secret_access_key, region_name, StreamName")

    def init_app(self, app):
        if hasattr(app, "teardown_appcontext"):
            app.teardown_appcontext(self.send_events)
        else:
            app.teardown_request(self.send_events)

    def event(self, evt):
        self.queue.put_nowait(evt)

    def send_events(self, Response):
        while True:
            try:
                evt = self.queue.get_nowait()
            except Empty:
                break

            self.kinesis.put_record(DeliveryStreamName=self.StreamName,
                                    Record={"Data": json.dumps(evt)},
                                    PartitionKey=str(hash(json.dumps(evt))))
        return Response

    def before_request(self):
        g.events = self

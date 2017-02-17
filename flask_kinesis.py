# coding: utf8
import boto3
from Queue import Queue


class kinesis(object):

    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app)
            app.after_request(self.send_events)

            self.queue = Queue()
            try:
                self.kinesis = boto3.client('firehose',
                                            aws_access_key_id=kwargs['aws_access_key_id'],
                                            aws_secret_access_key=kwargs['aws_secret_access_key'],
                                            region=kwargs['region'])
                self.StreamName = kwargs['StreamName']
            except:
                raise TypeError("aws_access_key_id, aws_secret_access_key, region, StreamName")

    def init_app(self, app):
        if hasattr(app, "teardown_appcontext"):
            app.teardown_appcontext(self.send_events)
        else:
            app.teardown_request(self.send_events)

    def event(self, evt):
        self.queue(evt)

    def send_events(self, exception):
        while True:
            try:
                evt = self.queue.get_nowait()
            except Empty:
                break
        return Exception

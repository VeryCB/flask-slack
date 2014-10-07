from pytest import fixture
from flask import Flask

from flask_slack import Slack


class App(object):

    def __init__(self):
        self.app = Flask(__name__)
        self.app.debug = True
        self.slack = Slack(self.app)
        self.app.add_url_rule('/', view_func=self.slack.dispatch)
        self.client = self.app.test_client()


@fixture
def app():
    return App()


def test_register_command(app):
    res = app.client.get('/')
    assert res.status_code == 200
    assert res.data == b'Command None is not found in team None'

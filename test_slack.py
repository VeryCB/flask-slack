from pytest import fixture, raises
from flask import Flask
from six import b

from flask_slack import Slack


class App(object):

    def __init__(self):
        self.app = Flask(__name__)
        self.app.debug = True
        self.slack = Slack(self.app)
        self.app.add_url_rule('/', view_func=self.slack.dispatch)
        self.client = self.app.test_client()


@fixture(scope='module')
def app():
    return App()


def test_request_without_registering_commands(app):
    res = app.client.get('/')
    assert res.status_code == 200
    assert res.data == b('Command None is not found in team None')


def test_registering_commands(app):
    command = 'sing'
    token = 'mytoken'
    team_id = 'MYTEAMID'
    methods = ['POST']
    text = 'little apple'

    get_url = '/?token={0}&team_id={1}&command={2}&text={3}'.format(
        token, team_id, command, text)

    @app.slack.command(command, token, team_id, methods)
    def _sing_a_song(**kwargs):
        lyrics = 'You are my littttle apple...'
        return app.slack.response(lyrics)

    expected_commands = {
        (team_id, command): (_sing_a_song, token, methods, {}),
    }

    assert app.slack._commands == expected_commands

    get_res = app.client.get(get_url)

    assert get_res.status_code == 200
    assert get_res.data == b('GET request is not allowed')

    post_data = {
        'command': command,
        'token': token,
        'team_id': team_id,
        'text': text
    }

    post_res = app.client.post('/', data=post_data)

    assert post_res.status_code == 200
    assert post_res.data == b('You are my littttle apple...')


def test_commands_without_registering_team_id(app):
    command = 'sing'
    token = 'mytoken'
    methods = ['POST']

    with raises(RuntimeError):
        @app.slack.command(command, token, methods=methods)
        def _sing_a_song(**kwargs):
            lyrics = 'You are my littttle apple...'
            return app.slack.response(lyrics)


def test_invalid_token(app):
    command = 'sing'
    token = 'mytoken'
    team_id = 'MYTEAMID'
    methods = ['POST']
    text = 'little apple'

    invalid_token = 'myinvalidtoken'

    @app.slack.command(command, token, team_id, methods)
    def _sing_a_song(**kwargs):
        lyrics = 'You are my littttle apple...'
        return app.slack.response(lyrics)

    post_data = {
        'command': command,
        'token': invalid_token,
        'team_id': team_id,
        'text': text
    }

    post_res = app.client.post('/', data=post_data)

    assert post_res.status_code == 200
    assert post_res.data == b('Your token {} is invalid'.format(invalid_token))

"""
    flaskext.slack
    ~~~~~~~~~~~~~~~

    Slack exntension for Flask.

    :copyright: (c) 2014 by VeryCB.
    :license: BSD, see LICENSE for more details.
"""

__all__ = ('Slack',)
__version__ = '0.1.0'
__author__ = 'VeryCB <imcaibin@gmail.com>'


class Slack(object):

    def __init__(self, app=None):
        self._commands = {}
        self.team_id = None

        if app:
            self.init_app(app)

    def init_app(self, app=None):
        config = getattr(app, 'config', app)

        self.team_id = config.get('TEAM_ID')

    def command(self, command, token, team_id=None, methods=['GET'], **kwargs):
        if team_id is None:
            team_id = self.team_id
        if team_id is None:
            raise RuntimeError('TEAM_ID is not found in your configuration!')

        def deco(func):
            self._commands[(team_id, command)] = (func, token, methods, kwargs)
            return func
        return deco

    def dispatch(self):
        from flask import request

        method = request.method

        data = request.args
        if method == 'POST':
            data = request.form

        token = data.get('token')
        team_id = data.get('team_id')
        command = data.get('command')

        if isinstance(command, basestring):
            command = command.strip().lstrip('/')

        try:
            self.validate(command, token, team_id, method)
        except RuntimeError as e:
            return self.response(e.message)

        func, _, _, kwargs = self._commands[(team_id, command)]
        kwargs.update(data.to_dict())

        return func(**kwargs)

    dispatch.methods = ['GET', 'POST']

    def validate(self, command, token, team_id, method):
        if (team_id, command) not in self._commands:
            raise RuntimeError('Command {0} is not found in team {1}'.format(
                               command, team_id))

        func, _token, methods, kwargs = self._commands[(team_id, command)]

        if method not in methods:
            raise RuntimeError('{} request is not allowed'.format(method))

        if token != _token:
            raise RuntimeError('Your token {} is invalid'.format(token))

    def response(self, text):
        from flask import Response
        return Response(text, content_type='text/plain; charset=utf-8')

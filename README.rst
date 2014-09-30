Flask-Slack
============

UNDER DEVELOPMENT, API WILL CHANGE!

Flask-Slack is a Flask extension which makes it easy to interact with Slack slash commands.


Installation
------------

You can install Flask-Slack with pip::

    $ pip install flask-slack

Or, with setuptools easy_install in case you didn't have pip::

    $ easy_install flask-slack


Usage
-----
::

    from flask_slack import Slack


    slack = Slack(app)
    app.add_url_rule('/', view_func=slack.dispatch)


    @slack.command('your_command', token='your_token',
                   team_id='your_team_id', methods=['POST'])
    def your_method(**kwargs):
        text = kwargs.get('text')
        return slack.response(text)

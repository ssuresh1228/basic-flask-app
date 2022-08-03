from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello World'


@application.route('/readme')
def newpage():
    return 'this is a new page'

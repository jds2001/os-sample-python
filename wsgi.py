from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route('/world')
def world():
    return 'World Hello'

@application.route('/getme')
def getme:
    return 'getme'


if __name__ == "__main__":
    application.run()

#!flask/bin/python
import os
import optparse

from app import init_app
# from flaskrun import flaskrun

# application = init_app()

# if __name__ == '__main__':
#     flaskrun(application)


config_name = os.getenv('FLASK_CONFIG')
default_host = "0.0.0.0"
default_port = "8080"

# Set up the command-line options
parser = optparse.OptionParser()
msg = 'Hostname of Flask app [{}]'.format(default_host)
parser.add_option("-H", "--host",
                  help=msg,
                  default=default_host)
msg = 'Port for Flask app [{}]'.format(default_port)
parser.add_option("-P", "--port",
                  help=msg,
                  default=default_port)
parser.add_option("-d", "--debug",
                  action="store_true", dest="debug",
                  help=optparse.SUPPRESS_HELP)

options, _ = parser.parse_args()

application = init_app()

if __name__ == '__main__':
    application.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )
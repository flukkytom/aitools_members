from flask import Flask, render_template, abort, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail() # instantiate the mail class

from .models.model import AiToolsMember

def init_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    Bootstrap(app)
    login_manager.init_app(app)
    
    # set a 'SECRET_KEY' to enable the Flask session cookies
    app.config['SECRET_KEY'] = 'skloud!!w@11'

    # Login user configuration settings
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "aitools_app.login"
    login_manager.refresh_view = 'aitools_app.login'
    login_manager.needs_refresh_message = (u"Session timedout, please re-login")
    login_manager.needs_refresh_message_category = "info"

    @login_manager.user_loader
    def load_user(id):
        return AiToolsMember.query.filter_by(id=id).first()

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=30)

    # BluePrints
    from .routes import aitools_app as aitools_blueprint
    app.register_blueprint(aitools_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/404.html', title='Forbidden'), 404

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/404.html', title='Server Error'), 404
        
    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from RuneScrapeWeb.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	
	db.init_app(app)
	bcrypt.init_app(app)
	mail.init_app(app)

	#Import the blueprint instance
	from RuneScrapeWeb.main.routes import main
	from RuneScrapeWeb.items.routes import items
	from RuneScrapeWeb.errors.handlers import errors
	app.register_blueprint(main)
	app.register_blueprint(items)
	app.register_blueprint(errors)

	return app
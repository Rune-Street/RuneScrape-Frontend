import os

class Config:
	SECRET_KEY = 'M%lraz@Lj)_UoMa'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	RUNESCRAPE_API = "https://runescrape.dev.bob.analogsea.ca"
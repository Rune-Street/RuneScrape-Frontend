from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
	pass
	
@main.route("/about")
def about():
	return render_template("about.html")
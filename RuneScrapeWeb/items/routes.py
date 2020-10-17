import requests

from os import path
from flask import Blueprint, render_template, jsonify, redirect

from RuneScrapeWeb.config import Config
from RuneScrapeWeb.url_helper import Url_Helper

items = Blueprint('items', __name__)

@items.route("/items")
def all_items():
	request_url = Url_Helper.join(Config.RUNESCRAPE_API, "items")
	resp = requests.get(request_url)
	data = resp.json()

	return render_template('items.html', items=data)

@items.route("/item/<string:item_name>")
def item(item_name):
	request_url = Url_Helper.join(Config.RUNESCRAPE_API, "item", item_name, "history", "day", "2", "view", "item.html")
	return redirect(request_url)
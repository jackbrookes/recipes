from flask import Flask

application = Flask(__name__)
application.config["FREEZER_BASE_URL"] = "https://jbrookes.com/recipes"

from app import routes
from flask import Flask
from rps.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from rps import routes

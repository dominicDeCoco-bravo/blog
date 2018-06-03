from flask import Flask
from config import Configuration
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Configuration)
CORS(app)
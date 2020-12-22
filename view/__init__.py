from flask import Flask


app = Flask(__name__)

import view.api_routes
import view.html_routes







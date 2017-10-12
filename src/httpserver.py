from flask import Flask
from webhook.github import Webhook


app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app)  # Defines '/postreceive' endpoint


def run_server(host="0.0.0.0", port=8888):
    app.run(host=host, port=port, debug=True)

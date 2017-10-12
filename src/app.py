from flask import Flask
from webhook.github import Webhook

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app)  # Defines '/postreceive' endpoint


def run(host="0.0.0.0", port=8888):
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    run()

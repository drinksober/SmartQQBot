from flask import Flask
from webhook import webhook

app = Flask(__name__)  # Standard Flask app

app.route('/postreceive', methods=['POST'])(webhook.view)


def run(host="0.0.0.0", port=8888):
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    run()

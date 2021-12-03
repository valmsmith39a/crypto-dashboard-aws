import json
from flask import Flask, request
from flask_cors import CORS
from models import setup_db, Token


application = Flask(__name__)
# setup_db(application)
CORS(application)


@application.route("/")
def home():
    return "Welcome to the metaverse."


@application.route("/api/tokens")
def get_tokens():
    return {
        "tokens": [
            {
                "name": "Bitcoin",
                "symbol": "BTC",
                "price": "64,000",
                "sentiment_score": "89",
            },
            {
                "name": "Ethereum",
                "symbol": "ETH",
                "price": "3900",
                "sentiment_score": "80",
            },
        ]
    }


if __name__ == "__main__":
    application.run()

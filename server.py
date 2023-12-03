from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Mock database (a simple list of URLs)
mock_db = [
    {"id": 1, "url": "https://example.com"},
    {"id": 2, "url": "https://openai.com"},
    {"id": 3, "url": "https://news.ycombinator.com"},
    {"id": 4, "url": "https://github.com"},
    {"id": 5, "url": "https://stackoverflow.com"},
    {"id": 6, "url": "https://www.reddit.com"},
    {"id": 7, "url": "https://www.medium.com"},
    {"id": 8, "url": "https://www.wikipedia.org"},
    {"id": 9, "url": "https://www.netflix.com"},
    {"id": 10, "url": "https://www.amazon.com"},
    {"id": 11, "url": "https://www.google.com"},
    {"id": 12, "url": "https://www.facebook.com"},
    {"id": 13, "url": "https://www.twitter.com"},
    {"id": 14, "url": "https://www.linkedin.com"},
    {"id": 15, "url": "https://www.instagram.com"},
    {"id": 16, "url": "https://www.pinterest.com"},
    {"id": 17, "url": "https://www.spotify.com"},
    {"id": 18, "url": "https://www.apple.com"},
    {"id": 19, "url": "https://www.microsoft.com"},
    {"id": 20, "url": "https://www.adobe.com"},
]


def normalize_url(url):
    # Remove 'www.' prefix and trailing slash for consistent matching
    if url.startswith("www."):
        url = url[4:]
    if url.endswith("/"):
        url = url[:-1]
    return url.lower()


@app.route("/check", methods=["GET"])
def check_url():
    url_to_check = normalize_url(request.args.get("url", ""))
    url_exists = any(normalize_url(url["url"]) == url_to_check for url in mock_db)
    return jsonify({"exists": url_exists}), 200


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def connect_db():
    return sqlite3.connect("admin_panel.db")


def normalize_url(url):
    # Remove 'https://' or 'http://' prefix, 'www.' prefix, and trailing slash for consistent matching
    if url.startswith("https://"):
        url = url.replace("https://", "", 1)
    elif url.startswith("http://"):
        url = url.replace("http://", "", 1)

    if url.startswith("www."):
        url = url[4:]

    if url.endswith("/"):
        url = url[:-1]

    return url.lower()


@app.route("/check", methods=["GET"])
def check_url():
    url_to_check = normalize_url(request.args.get("url", ""))
    conn = connect_db()
    c = conn.cursor()

    # Assuming the URLs are stored in the 'name' column of the 'Channels' table
    c.execute("SELECT name FROM Channels")
    channels = c.fetchall()

    url_exists = any(normalize_url(channel[0]) == url_to_check for channel in channels)
    conn.close()

    return jsonify({"exists": url_exists}), 200


if __name__ == "__main__":
    app.run(debug=True)

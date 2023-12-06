from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def connect_db():
    return sqlite3.connect("admin_panel.db")


def normalize_url(url):
    # Modify this normalization to match how URLs are stored in your database
    return url.lower().strip()


@app.route("/check", methods=["GET"])
def check_url():
    url_to_check = request.args.get("url", "")
    conn = connect_db()
    c = conn.cursor()
    print("Checking URL:", url_to_check)

    # List of column names to check against
    columns = [
        "External_links",
        "Website",
        "Twitter",
        "Twitter_ID",
        "Facebook",
        "Threads",
        "YouTube",
        "YouTube_ID",
        "TikTok",
        "Instagram",
        "LinkedIn",
        "Reddit",
        "VK",
        "Telegram",
        "Substack",
        "Quora",
        "Patreon",
        "GoFundMe",
        "Paypal",
        "Twitch",
        "Mastadon",
        "Wechat",
        "QQ",
        "Douyin",
    ]

    url_exists = False
    for column in columns:
        query = f"SELECT {column} FROM Entities WHERE {column} = ?"
        print("Checking column:", column)  # Print the column being checked
        c.execute(query, (url_to_check,))
        result = c.fetchone()
        print("Result for", column, ":", result)  # Print the result for each column
        if result:
            url_exists = True
            break

    conn.close()
    return jsonify({"exists": url_exists}), 200


if __name__ == "__main__":
    app.run(debug=True)

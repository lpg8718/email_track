from flask import Flask, send_file, Response
import sqlite3
import os

app = Flask(__name__)

DB_FILE = "email.db"

@app.route("/")
def health():
    return "OK"

@app.route("/email/open/<tracking_id>/image")
def track_and_serve_image(tracking_id):
    # track open

    print("Open api........................")
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE email_tracking SET opened_at=datetime('now') WHERE id=? AND opened_at IS NULL",
            (tracking_id,)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("DB error:", e)

    # serve image
    image_path = "static/images/header.png"
    return send_file(image_path, mimetype="image/png", cache_timeout=0)

if __name__ == "__main__":
    app.run()

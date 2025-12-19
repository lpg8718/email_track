from flask import Flask, Response
import sqlite3

app = Flask(__name__)

DB_FILE = "email_tracking.db"

@app.route("/email/open/<tracking_id>.png")
def track_open(tracking_id):
    print("OPEN HIT:", tracking_id)

    # OPTIONAL DB update
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE email_tracking SET opened_at = datetime('now') WHERE id=?",
            (tracking_id,)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("DB error:", e)

    # 1x1 PNG
    pixel = (
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
        b'\x00\x00\x00\x01\x00\x00\x00\x01'
        b'\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
        b'\x00\x00\x00\nIDATx\x9cc`\x00\x00\x00\x02\x00\x01'
        b'\xe2!\xbc3\x00\x00\x00\x00IEND\xaeB`\x82'
    )

    response = Response(pixel, mimetype="image/png")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run()

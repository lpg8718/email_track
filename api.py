from flask import Flask, send_file, Response
import sqlite3
import os

app = Flask(__name__)


@app.route("/")
def health():
    return "OK"
PIXEL_BYTES = (
    b'\x89PNG\r\n\x1a\n'
    b'\x00\x00\x00\rIHDR'
    b'\x00\x00\x00\x01'  # width: 1
    b'\x00\x00\x00\x01'  # height: 1
    b'\x08\x06\x00\x00\x00'
    b'\x1f\x15\xc4\x89'
    b'\x00\x00\x00\nIDAT'
    b'\x08\xd7c\x00\x00\x00\x02\x00\x01'
    b'\xe2!\xbc\x33'
    b'\x00\x00\x00\x00IEND\xaeB`\x82'
)

@app.route("/pixel.png")
def tracking_pixel():
    print("............................................................")
    return Response(
        PIXEL_BYTES,
        mimetype="image/png",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )
@app.route("/test.png")
def test_png():
    print("IMAGE HIT..........")
    print("Entry in databse ..........")
    return Response(
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
        b'\x00\x00\x00\x01\x00\x00\x00\x01'
        b'\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
        b'\x00\x00\x00\nIDATx\x9cc`\x00\x00\x00\x02\x00\x01'
        b'\xe2!\xbc3\x00\x00\x00\x00IEND\xaeB`\x82',
        mimetype="image/png"
    )


if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database setup
conn = sqlite3.connect("form_data.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
"""
)
conn.commit()
conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")

    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)", (username, email)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Form data submitted successfully!"})


if __name__ == "__main__":
    app.run(debug=True)

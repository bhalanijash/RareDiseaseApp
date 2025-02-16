from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Flask App!"

@app.route("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")  # Ensure you have a 'users' table
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
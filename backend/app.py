from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return "Grocery Management System is running!"


@app.route("/api/products")
def get_products():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)

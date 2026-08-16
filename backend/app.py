from flask import Flask, jsonify, request
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

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json()

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO products (name, category, price, stock)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        data["name"],
        data["category"],
        data["price"],
        data["stock"]
    )

    cursor.execute(query, values)
    connection.commit()

    product_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Product added successfully",
        "product_id": product_id
    }), 201


if __name__ == "__main__":
    app.run(debug=True)

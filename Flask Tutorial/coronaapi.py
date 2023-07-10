#!/usr/bin/python
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS


def connect_to_db():
    conn = sqlite3.connect('coronadb1.db')
    return conn

def insert_product(corona):
    inserted_state = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO corona ( statename,active,recovered,death,total) VALUES (?, ?, ?, ?, ?)", (corona['statename'], corona['active'], corona['recovered'], corona['death'], corona['total']) )
        conn.commit()
        inserted_state = get_state_by_code(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_product


def get_products():
    states = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM corona")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            state = {}
            state["code"] = i["code"]
            state["statename"] = i["statename"]
            state["active"] = i["active"]
            state["recovered"] = i["recovered"]
            state["death"] = i["death"]
            state["total"] = i["total"]
            states.append(state)

    except:
        states = []

    return states


def get_state_by_code(code):
    state = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM corona WHERE code = ?", (code,))
        row = cur.fetchone()
        # convert row object to dictionary
        product["code"] = row["code"]
        product["name"] = row["name"]
        product["desc"] = row["desc"]
        product["supplier"] = row["supplier"]
        product["price"] = row["price"]
    except:
        product = {}

    return product


def update_product(product):
    updated_product = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE product SET name = ?, desc = ?, supplier = ?, price = ? WHERE code =?", (product["name"], product["desc"], product["supplier"], product["price"], product["code"],))
        conn.commit()
        #return the product
        updated_product = get_product_by_code(product["code"])

    except:
        conn.rollback()
        updated_product = {}
    finally:
        conn.close()

    return updated_product


def delete_product(product_code):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from product WHERE code = ?", (product_code,))
        conn.commit()
        message["status"] = "Product deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete product"
    finally:
        conn.close()

    return message

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/product', methods=['GET'])
def api_get_products():
    return jsonify(get_products())

@app.route('/api/product/<product_code>', methods=['GET'])
def api_get_product(product_code):
    return jsonify(get_product_by_code(product_code))

@app.route('/api/product',  methods = ['POST'])
def api_add_product():
    product = request.get_json()
    return jsonify(insert_product(product))

@app.route('/api/product',  methods = ['PUT'])
def api_update_product():
    product = request.get_json()
    return jsonify(update_product(product))

@app.route('/api/product/<product_code>',  methods = ['DELETE'])
def api_delete_product(product_code):
    return jsonify(delete_product(product_code))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()
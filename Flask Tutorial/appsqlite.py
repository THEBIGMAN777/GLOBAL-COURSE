#!/usr/bin/python
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS


def connect_to_db():
    conn = sqlite3.connect('coronadb1.db')
    return conn
def insert_state(corona):
    inserted_state = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO corona (statename, active, recovered, death,total) VALUES (?, ?, ?, ?, ?)", (corona['statename'], corona['active'], corona['recovered'], corona['death'], corona['total']) )
        conn.commit()
        inserted_state = get_state_by_code(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_state


def get_state():
    state = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM corona")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
             patient= {}
             patient["code"] = i["code"]
             patient["statename"] = i["statename"]
             patient["active"] = i["active"]
             patient["recovered"] = i["recovered"]
             patient["death"] = i["death"]
             patient["total"] = i["total"]
        state.append(patient)

    except:
        state = []

    return state


def get_state_by_code(code):
    state = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM corona WHERE code = ?", (code,))
        row = cur.fetchone()

        # convert row object to dictionary
        state["code"] = row["code"]
        state["statename"] = row["statename"]
        state["active"] = row["active"]
        state["recovered"] = row["recovered"]
        state["death"] = row["death"]
        state["total"] = row["total"]
    except:
        user = {}

    return state


def update_state(corona):
    updated_state = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE corona SET  statename = ?, active = ?, recovered = ?, death = ?, total = ? WHERE code =?", (corona["statename"], corona["active"], corona["recovered"], corona["death"], corona["total"], corona["code"],))
        conn.commit()
        #return the state
        updated_user = get_state_by_code(updated_state["code"])

    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()

    return updated_user


def delete_state(code):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from corona WHERE code = ?", (code,))
        conn.commit()
        message["status"] = "state deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete state"
    finally:
        conn.close()

    return message

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/state', methods=['GET'])
def api_get_users():
    return jsonify(get_state())

@app.route('/api/state/<code>', methods=['GET'])
def api_get_user(code):
    return jsonify(get_state_by_code(code))

@app.route('/api/state/add',  methods = ['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_state(user))

@app.route('/api/state/update',  methods = ['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_state(user))

@app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_state(user_id))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()
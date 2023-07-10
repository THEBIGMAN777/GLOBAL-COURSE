import sqlite3

def connect_to_db():
    conn = sqlite3.connect('coronadb1.db')
    return conn
def create_db_table():
    try:
        conn = connect_to_db()
        #conn.execute('''DROP TABLE corona''')
        conn.execute('''
            CREATE TABLE corona (
                code INTEGER PRIMARY KEY NOT NULL,
                statename TEXT NOT NULL,
                active INTEGER NOT NULL,
                recovered INTEGER NOT NULL,
                death INTEGER NOT NULL,
                total INTEGER NOT NULL
            );
        ''')

        conn.commit()
        print("corona table created successfully")
    except:
        print("corona table creation failed - Maybe table")
    finally:
        conn.close()

#create_db_table()
def get_state_by_code(code):
    patient = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM corona WHERE code = ?", (code,))
        row = cur.fetchone()

        # convert row object to dictionary
        patient["code"] = row["code"]
        patient["statename"] = row["statename"]
        patient["active"] = row["active"]
        patient["recovered"] = row["recovered"]
        patient["death"] = row["death"]
        patient["total"] = row["total"]
    except:
        patient = {}

    return patient


def insert_patient(corona):
    inserted_patient = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO corona ( statename, active, recovered, death,total) VALUES (?, ?, ?, ?, ?)", ( corona['statename'], corona['active'], corona['recovered'], corona['death'], corona['total']) )
        conn.commit()
        inserted_patient= get_state_by_code(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_patient
patients = []
patient0 = {
    "code": "1",
    "statename": "Andhra-Pradesh",
    "active": "067765665656",
    "recovered": "982891898",
    "death": "14845",
    "total": "1232"
}

patient1 = {
    "code": "2",
    "statename": "Karnataka",
    "active": "067765665656",
    "recovered": "19441955614",
    "death": "41514454",
    "total": "14165"
}

patient2 = {
    "code": "3",
    "statename": "Kerala",
    "active": "067765665656",
    "recovered": "198196548574",
    "death": "954554854",
    "total": "857454"
}

patient3 = {
    "code": "4",
    "statename": "Tamil-Nadu",
    "active": "067765665656",
    "recovered": "41959615656",
    "death": "545454",
    "total": "545454"
}

patients.append(patient0)
patients.append(patient1)
patients.append(patient2)
patients.append(patient3)
"""
"""
for i in patients:
    print(insert_patient(i))

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3, uuid

DB = 'auth.db'
app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id TEXT PRIMARY KEY,
                 username TEXT UNIQUE,
                 password TEXT
                 )''')
    conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        user_id = str(uuid.uuid4())
        c.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)', (user_id, username, password))
        conn.commit()
        return jsonify({'user_id': user_id}), 201
    except:
        return jsonify({'error': 'username exists'}), 409
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001)

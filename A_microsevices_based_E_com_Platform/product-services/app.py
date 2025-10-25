from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

DB = 'product.db'
app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 price REAL,
                 qty INTEGER
                 )''')
    c.execute('INSERT OR IGNORE INTO products (id,name,price,qty) VALUES (1,"Laptop",799.99,10)')
    conn.commit()
    conn.close()

@app.route('/products', methods=['GET'])
def list_products():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT id,name,price,qty FROM products')
    rows = c.fetchall()
    conn.close()
    return jsonify([{'id': r[0], 'name': r[1], 'price': r[2], 'qty': r[3]} for r in rows])

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5002)

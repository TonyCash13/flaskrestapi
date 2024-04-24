from flask import Flask, request, jsonify
import sqlite3
import json
app = Flask(__name__)
conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

conn.commit()

@app.route('/test', methods=['GET', 'POST'])
def poster():
    if request.method == 'POST':
        user = request.get_json()
        c = conn.cursor()
        c.execute(f"INSERT INTO example (name) VALUES (?)", (user['name'],))
        conn.commit()
        conn.close()
    return "Запись успешно добавлена"

@app.route('/test2', methods=['GET', 'POST'])
def getter():
    if request.method == 'GET':
        c = conn.cursor()
        result = c.execute("SELECT * FROM example")
        rows = c.fetchall()
    return rows

if __name__ == '__main__':
    app.debug = True
    app.run()
from flask import Flask, jsonify, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="db",
    port="5432"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/response-times')
def get_response_times():
    cur = conn.cursor()
    cur.execute("SELECT checked_at, response_time_ms FROM response_times")
    response_times = [{'checked_at': str(row[0]), 'response_time_ms': row[1]} for row in cur.fetchall()]
    cur.close()
    return jsonify(response_times)

if __name__ == '__main__':
    app.run(debug=True)

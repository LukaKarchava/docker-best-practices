from flask import Flask, jsonify, request
import psycopg2
import time
from datetime import datetime

app = Flask(__name__)

# The secret connection string to log into our database container over the virtual bridge
DB_URI = "postgresql://luka_admin:my_secure_password123@database_notebook:5432/visit_logs"

def init_db():
    # Connect to Postgres and create the blank paper table if it doesn't exist yet
    print("Waiting 5 seconds for Postgres to wake up...")
    time.sleep(5)
    conn = psycopg2.connect(DB_URI)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS site_visits (
            id SERIAL PRIMARY KEY,
            ip_address TEXT,
            device_info TEXT,
            visit_time TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def home():
    # 1. Grab visitor details from the incoming request
    visitor_ip = request.remote_addr
    visitor_device = request.headers.get('User-Agent')
    current_time = datetime.now()

    # 2. Open the notebook and write the logs down
    conn = psycopg2.connect(DB_URI)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO site_visits (ip_address, device_info, visit_time) VALUES (%s, %s, %s);",
        (visitor_ip, visitor_device, current_time)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "status": "connected",
        "message": "Hello from the Python backend container!",
        "location": "Tbilisi, Georgia - Managed by Luka  (CI/CD Verified!)",
        "log_status": "Visit successfully written down in the Postgres database!"
    })

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

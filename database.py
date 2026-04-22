import mysql.connector
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",        # <-- change to your MySQL password
    "database": "smart_irrigation_db"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def save_moisture_reading(sensor_id, moisture, weather, pump_status, tank_level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO moisture_data (sensor_id, moisture_value, weather, pump_status, tank_level) VALUES (%s, %s, %s, %s, %s)",
        (sensor_id, moisture, weather, pump_status, tank_level)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_history(limit=20):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM moisture_data ORDER BY timestamp DESC LIMIT %s", (limit,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Convert datetime to string
    for row in rows:
        row["timestamp"] = str(row["timestamp"])
    return rows

def log_message(message):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO system_logs (message) VALUES (%s)", (message,))
    conn.commit()
    cursor.close()
    conn.close()

def get_logs(limit=10):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM system_logs ORDER BY timestamp DESC LIMIT %s", (limit,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in rows:
        row["timestamp"] = str(row["timestamp"])
    return rows

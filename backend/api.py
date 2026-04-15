from fastapi import FastAPI
import psycopg2

app = FastAPI()

# DB connection
def get_connection():
    return psycopg2.connect(
        dbname="iot_db",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

# Get latest data
@app.get("/latest")
def get_latest():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, temperature, humidity
        FROM sensor_data
        ORDER BY timestamp DESC
        LIMIT 1
    """)

    row = cur.fetchone()
    conn.close()

    return {
        "timestamp": row[0],
        "temperature": row[1],
        "humidity": row[2]
    }

# Get all data
@app.get("/data")
def get_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, temperature, humidity
        FROM sensor_data
        ORDER BY timestamp DESC
        LIMIT 100
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "timestamp": r[0],
            "temperature": r[1],
            "humidity": r[2]
        } for r in rows
    ]
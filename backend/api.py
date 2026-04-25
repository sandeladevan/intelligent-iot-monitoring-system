from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    while True:
        try:
            return psycopg2.connect(
                host="db",
                database="iot_data",
                user="postgres",
                password="1234"
            )
        except:
            time.sleep(2)

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
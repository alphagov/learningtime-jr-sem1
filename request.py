import requests
import time
import psycopg2

def check_endpoint(url):
    conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="db",
            port="5432"
        )
    with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS response_times (
                        id SERIAL PRIMARY KEY,
                        url VARCHAR(255) NOT NULL,
                        response_code INTEGER NOT NULL,
                        response_time_ms REAL NOT NULL,
                        checked_at TIMESTAMP NOT NULL
                    );
                """)
                conn.commit()
    try:
        response = requests.get(url, timeout=5).status_code
        response_time_ms = response.elapsed.total_seconds() * 1000
    except requests.exceptions.RequestException as e:
       response = 500
       response_time_ms = 0
    with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO response_times (url, response_code, response_time_ms, checked_at)
                    VALUES (%s, %s, %s, NOW());
                """, (url, response, response_time_ms))
                conn.commit()
    conn.close()

url_to_check = 'https://www.python.org'

while True:
    check_endpoint(url_to_check)
    time.sleep(60)
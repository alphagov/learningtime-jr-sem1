import requests
import time
import psycopg2

def check_endpoint(url):
    try:
        response = requests.get(url, timeout=5)
        response_time_ms = response.elapsed.total_seconds() * 1000
        
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="db",
            port="5432"
        )
        
        try:
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
        
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO response_times (url, response_code, response_time_ms, checked_at)
                    VALUES (%s, %s, %s, NOW());
                """, (url, response.status_code, response_time_ms))
                conn.commit()

        except Exception as e:
            print(f"Database operation failed: {str(e)}")
        finally:
            conn.close()
            
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed. Error: {str(e)}")

url_to_check = 'https://www.python.org'

while True:
    check_endpoint(url_to_check)
    time.sleep(60)
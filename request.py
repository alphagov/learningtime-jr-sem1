import requests
import time
import psycopg2

def check_endpoint(url):
    try:
        response = requests.get(url, timeout=5)
        response_time_ms = response.elapsed.total_seconds() * 1000

        connector = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="db",
            port="5432"
        )
        
        with connector.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS response_times (
                    id SERIAL PRIMARY KEY,
                    url VARCHAR(255) NOT NULL,
                    response_code INTEGER NOT NULL,
                    response_time_ms REAL NOT NULL,
                    checked_at TIMESTAMP NOT NULL
                );
            """)
            connector.commit()

        with connector.cursor() as cursor:
            cursor.execute("""
                INSERT INTO response_times (url, response_code, response_time_ms, checked_at)
                VALUES (%s, %s, %s, NOW());
            """, (url, response.status_code, response_time_ms))
            connector.commit()
        
        connector.close()

        if response.status_code == 200:
            print(f"The endpoint {url} is healthy. Response time: {response_time_ms:.0f} ms.")
        else:
            print(f"The endpoint {url} returned status code: {response.status_code}. Response time: {response_time_ms:.0f} ms.")

    except requests.exceptions.RequestException as exception:
        print(f"Request to {url} failed. Error: {str(exception)}")

url_to_check = 'https://www.python.org'

while True:
    check_endpoint(url_to_check)
    time.sleep(60)
import requests
import time

def check_endpoint(url):
    try:
        response = requests.get(url, timeout=5)
        response_time_ms = response.elapsed.total_seconds() * 1000
        
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
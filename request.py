import requests
import time

def check_endpoint(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"The endpoint {url} is healthy.")
        else:
            print(f"The endpoint {url} returned status code: {response.status_code}.")
    except requests.exceptions.RequestException as exception:
        print(f"Request to {url} failed. Error: {str(exception)}")

url_to_check = 'https://www.python.org'

while True:
    check_endpoint(url_to_check)
    time.sleep(60)
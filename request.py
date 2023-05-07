import requests
def check_endpoint(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"The endpoint {url} is healthy.")
        else:
            print(f"The endpoint {url} returned status code: {response.status_code}.")
    except requests.exceptions.RequestException as exception:
        print(f"Request to {url} failed. Error: {str(exception)}")

check_endpoint('https://www.python.org')
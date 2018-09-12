import requests

if __name__ == '__main__':
    url = "http://localhost:8080"
    print(requests.get(url).text)

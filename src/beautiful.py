from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://ja.wikipedia.org/wiki/Hello_world"
    f = requests.get(url)

    soup = BeautifulSoup(f.content, "html.parser")
    value = soup.find("h1").text.title()
    print(value)

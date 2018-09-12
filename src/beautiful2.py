from bs4 import BeautifulSoup
import requests


def make_hello_world(urls, locations):
    #  結果を保持する変数
    result = ""
    #  取得する文字列のあるHTML要素(今回はタイトル部分のクラス名)
    target = "firstHeading"
    for index, url in enumerate(urls):
        url = "https://en.wikipedia.org/wiki/" + url
        f = requests.get(url)
        soup = BeautifulSoup(f.content, "html.parser")
        value = soup.find(class_=target).text
        result += value[locations[index]]
    return result


if __name__ == '__main__':
    urls = ["Harry_Potter",
            "The_Human_Centipede_(First_Sequence)",
            "Flying_Spaghetti_Monster",
            "Lil_Wayne",
            "Konjac",
            "Null_pointer",
            "Wikipedia",
            "Morgan_Freeman",
            "Starbucks",
            "Family_Guy",
            "Angry_Birds"]
    # タイトルの何文字目にターゲットの文字があるかを保持
    locations = [0, 2, 1, 2, 1, 4, 0, 1, 3, 4, 9]
    print(make_hello_world(urls, locations))

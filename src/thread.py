import threading


class HelloWorldCallable:
    def __init__(self, num):
        self.message = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
        self._num = num

    def call(self, results: list):
        results.append((self._num, self.message[self._num]))


if __name__ == "__main__":
    # 結果を格納する変数
    hello_list = []
    # 皆さんはちゃんと関数ベースにするかClass呼び出しにするかしましょう
    threads_list = []
    for _ in range(11):
        threads_list.append(
            threading.Thread(target=HelloWorldCallable(_).call(hello_list)))
    try:
        for thread in threads_list:
            thread.start()
        for thread in threads_list:
            thread.join()
        hello_list.sort()
        hello_str = ""
        for x in hello_list:
            hello_str += x[1]
        print(hello_str)
    except Exception as e:
        print(e)

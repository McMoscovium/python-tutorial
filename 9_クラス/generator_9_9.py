"""9.9. ジェネレーター

イテレーターを作成するための強力なツール"""


def ex1():
    """ジェネレーターの作成"""

    # 　__iter__メソッドと__next__メソッドを自動で作成する
    # 最後に StopIteration 例外を送出する
    def reverse(data):
        for index in range(len(data) - 1, -1, -1):
            yield data[index]

    for char in reverse("golf"):
        print(char)


def ex2():
    """ジェネレータ式"""

    x: int = sum(i * i for i in range(10))
    print(f"{x=}")

    # 上はこれと同じ
    def sq_sum(r: int):
        for i in range(r):
            yield i * i

    y: int = sum(sq_sum(10))
    print(f"{y=}")


if __name__ == "__main__":
    ex2()

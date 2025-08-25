"""9.8. イテレータ"""


def ex1():
    """イテレータの観察"""

    s = "abc"
    # iter() でイテレータを取得する
    it = iter(s)
    print(f"{it=}")
    print(f"{next(it)=}")
    print(f"{next(it)=}")
    print(f"{next(it)=}")

    # StopIteration 例外
    next(it)


def ex2():
    """イテレータの組み込み方

    __next__()メソッドをもつオブジェクトを返す__iter__()メソッドを追加すればよい"""

    class Reverse:
        """シーケンスを後ろから回るイテレーター"""

        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

    rev = Reverse("spam")
    print(f"{iter(rev)}")

    for char in rev:
        print(char)


if __name__ == "__main__":
    ex2()

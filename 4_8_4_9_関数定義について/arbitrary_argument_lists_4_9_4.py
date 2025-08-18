"""
4.9.4. 任意引数リスト
関数呼び出しを任意個数の引数で行えるようにする方法

4.9.5. 引数リストのアンパック
位置専用引数を要求する関数にリスト、タプル、辞書の形の引数を渡すために
リスト、タプル、辞書をアンパックする方法
"""


def ex1():
    def f(n, *args):
        print("n =", n)

        for item in args:
            print(item, end=", ")

        print("\n")

    def g(n, *args, kwd=""):
        f(n, *args)

        print("kwd =", kwd)
        print("\n")

    """
    * これらの *args が任意個数の引数を受け取る
    * *args より後の仮引数はキーワード専用引数になる。
    * *args に渡された引数はタプル args に格納される。
    """

    f(1, "a", "b", "c")
    f(1, *("a", "b", "c"))  # 上と同じ
    g(2, "d", "e", "f", kwd="キーワード")


# リスト、タプル、辞書のアンパック方法
def ex2() -> None:
    def add(a: int, b: int, /) -> int:
        """位置専用仮引数ver"""
        return a + b

    def add2(*, l: int, r: int):
        """キーワード専用仮引数ver"""
        return l + r

    lst: list[int] = [1, 2]
    tpl: tuple = (1, 2)
    dct: dict[str, int] = {"l": 1, "r": 2}

    # print(add(lst)) # エラー
    print(add(*lst))  # * でリストをアンパックする
    print(add(*tpl))  # * でタプルをアンパックする

    # print(add2(*lst))  # エラー
    print(add2(**dct))
    # print(add2(dct))  # エラー


if __name__ == "__main__":
    ex2()

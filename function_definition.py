# 関数定義について
# https://docs.python.org/ja/3.13/tutorial/controlflow.html#defining-functions


# docstringについて
def ex0():
    def f():
        """なにもしない"""
        pass

    print(f.__doc__)  # 「なにもしない」


# デフォルト引数は関数定義の時点で、関数を定義している側のスコープで評価される：
def ex1() -> None:
    i = 5

    def f(arg=i) -> None:
        print(arg)

    print(f.__defaults__)  # (5,)
    # この時点で f のデフォルト引数 arg は 5 である
    i = 6
    print(f.__defaults__)  # (5,)
    f()  # 5


# デフォルト引数は関数定義の時に1度だけ評価される：
def ex2() -> None:
    def f(a, L=[], M=[]):
        L.append(a)
        return L

    print(f.__defaults__)  # ([], [])
    # この時点で、fのデフォルト引数 L は [] である

    print(f(1))  # L = [1]
    print(f.__defaults__)  # ([1], [])

    print(f(2))  # L = [2]
    print(f.__defaults__)  # ([1,2], [])


# 後続の関数呼び出しでデフォルト引数を更新しない方法
def ex3():
    def f(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L

    print(f(1))  # [1]
    print(f.__defaults__)  # (None,)

    print(f(2))  # [2]
    print(f.__defaults__)  # (None,)


if __name__ == "__main__":
    ex3()

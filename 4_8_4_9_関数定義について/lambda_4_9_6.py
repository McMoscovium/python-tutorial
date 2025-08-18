"""
4.9.6. ラムダ式
https://docs.python.org/ja/3.13/tutorial/controlflow.html#lambda-expressions
"""


# ラムダ式は関数オブジェクトである。
def ex1():
    def make_incrementor(n: int):
        """n インクリメントする関数を返す関数"""
        return lambda x: x + n

    f = make_incrementor(1)
    g = lambda x: x + 2

    print(f(1))  # 2
    print(f(2))  # 3
    print(g(1))  # 3
    print(g(2))  # 4

    # ラムダ式自体が <lambda> という名前の関数オブジェクトである。
    print("f.__name =", f.__name__)  # <lambda>
    print("(lambda x: x + 1).__name__ =", (lambda x: x + 1).__name__)  # <lambda>
    print("(lambda x: x + 1).__defaults__ =", (lambda x: x + 1).__defaults__)  # None

    # ラムダ式は関数オブジェクトなので、通常のユーザー定義関数と同じ属性を持つ
    # 例えば、関数内のローカル変数の名前（仮引数を含む）のタプルを得ることができる
    print(
        "(lambda x:x+1).__code__.co_varnames =",
        (lambda x: {x + 1}).__code__.co_varnames,
    )  # ('x',)


if __name__ == "__main__":
    ex1()

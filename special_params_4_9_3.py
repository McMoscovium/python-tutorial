"""
4.9.3 特殊なパラメータ
https://docs.python.org/ja/3.13/tutorial/controlflow.html#special-parameters
"""


# 引数の渡され方の制限
# /, * を用いて引数の渡され方を指定する。
# /, *はこの順番のみ許される
# 何も指定しない場合、pos_or_kwdの扱いになる。
def ex1():
    def f(pos, /, pos_or_kwd, *, kwd):
        """
        pos に渡される引数はその位置で判断される

        pos_or_kwd に渡される引数は位置でもキーワードでも明示できる

        kwd はキーワードによる明示でのみ引数を受け取る
        """
        pass

    # 以下の定義も許される。
    def g(pos, /):
        pass

    def h(*, kwd):
        pass

    # invalidな引数で関数呼び出しをした場合、できの良いリンタ―はエラーを出してくれるので、試してごらん。


# 引数の渡し方によっては衝突がありうる
# 位置専用引数は、その名前に意味がない場合に使うべき
def ex2():
    # 引数に衝突ができうる関数の例
    def f(name, **kwds):
        return "name" in kwds

    # f(1, **{"name": ""}) # エラー
    # 理由はわからないが、おそらくこの引数は
    # f(1, name="") と展開されるのだろう

    def g(name, /, **kwds):
        return "name" in kwds

    print(g(1, **{"name": ""}))


# 引数に意味がある場合、キーワード専用引数を使うべき？
def ex3():
    def rational(*, num: int, denom: int) -> dict[int, int]:
        """
        簡易的に有理数を返す関数
        （本当はもちろん、 Rational クラスを返すべき！）
        """
        return {num: num, denom: denom}

    # rational(3,2) # エラー。どちらが分母かわかりにくい

    print(rational(num=3, denom=2))  # 分かりやすいが、長い（これくらいは我慢すべき？）


if __name__ == "__main__":
    ex2()

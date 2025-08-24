"""9.2.1. スコープと名前空間の例"""

"""チュートリアルの良くわからない説明について

Pythonの名前探索にはLEGBルール（Local→Enclosing→Global→Built-in）
というのに従っているらしい

- Local（最内スコープ）：実行中の関数や内包表記などのローカルなスコープ
- Enclosing（外側のスコープ）：ネストされた関数の、外側の関数のローカル変数
（ネストがなければこれはないので、３つか４つ）
- Global（グローバル）：モジュールレベルの名前空間
- Built-in：「len」「print」などのbuiltinモジュールの名前空間
"""


def ex1():
    """local, nonlocal, globalの違い"""

    def scope_test():
        def do_local():
            # do_local内に束縛された変数
            spam = "local spam"

        def do_nonlocal():
            # 1つ外（scope_test 内に束縛）
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            # これは、モジュールのグローバル名前空間に束縛される
            # よって、 ex1 の外でも使える
            global spam
            spam = "global spam"

        spam = "test spam"

        do_local()
        print("after do_local() :", spam)
        # test spam

        do_nonlocal()
        print("after do_nonlocal() :", spam)
        # nonlocal spam

        do_global()
        print("after do_global() :", spam)

    scope_test()
    print("In global scope:", spam)


def ex2():
    """外側のスコープにあって、nonlocal 宣言のない変数は読み出し専用"""
    x = 1

    def f():
        # このスコープでは nonlocal宣言のない x は読み出し専用

        # 読み出し可能
        print(x)

        # 変更不可能
        # x = x + 1

    f()


if __name__ == "__main__":
    ex2()

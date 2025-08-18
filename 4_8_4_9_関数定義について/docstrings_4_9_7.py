"""
4.9.7. ドキュメンテーション文字列
https://docs.python.org/ja/3.13/tutorial/controlflow.html#documentation-strings
"""


# 慣習であるが、まとめである最初の行は大文字で始まり、ピリオドで終わる必要がある。
# 2行目以降を書く場合は2行目を空行にする
# 最初の行の、空でない次の行がそのドキュメントのインデント量を決める。
# 私が使っているフォーマッタがドキュメントのインデントを許さないので、非自明なインデントのある例を作れない😢
def ex1() -> None:
    def f() -> None:
        """The first line.

        An example of docstring.
        Supplementary paragraph.
        """

    print(f.__doc__)  # このドキュメントのインデント量は0である


if __name__ == "__main__":
    ex1()

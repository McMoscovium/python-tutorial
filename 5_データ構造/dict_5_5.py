"""5.5. 辞書型

https://docs.python.org/ja/3.13/tutorial/datastructures.html#dictionaries"""


def ex1() -> None:
    """辞書型の利用例"""

    # 直接的な定義
    d: dict[str, int] = {"a": 1, "b": 2}

    # dict()コンストラクタを用いた定義
    e = dict([("name", "chimpo"), ("age", 8)])
    print(dict(taro=2, chimpo=16))

    # 内包的な定義
    print({x: x**2 for x in (2, 4, 6)})
    print({s: len(s) for s in ["chimpo", "taro"]})

    # ペアの追加
    d["c"] = 3

    # ペアの削除
    del d["c"]
    print(d)

    # キーのリスト
    print(list(d))

    # キーのタプル(一般にはリストよりタプルの方がいいと思う)
    print(tuple(d))

    # 指定したキーが含まれるかどうか
    print("a" in d)
    print("z" in d)


def ex2() -> None:
    # キーの型は異なっていてもよい
    d = {"a": 1, 1: 2}
    print(d)
    print(list(d))

    # リストをキーにはできない
    # e = {[a, b]: 1} # TypeError: unhashable type: 'list

    # 一般に、変更可能なオブジェクトはキーにできない
    # e = {(1, [1, 2]): 1}  # エラー。リンタ―に指摘されず、実行時にわかった

    # キーは辞書に追加した時点で評価され、変更できない
    a = 1
    e = {a: 1}
    print(e)  # {1: 1}
    a = 2
    print(e)  # {1: 1}


if __name__ == "__main__":
    ex1()

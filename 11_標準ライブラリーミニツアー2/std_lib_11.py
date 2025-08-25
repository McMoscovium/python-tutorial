"""11. 標準ライブラリミニツアー２"""


def ex1():
    """reprlib - 大きなコンテナや深くネストしたコンテナを
    省略して表示するバージョンのrepr()"""
    import reprlib

    x = reprlib.repr(set("aihisdflviasdhlvfiasheoghldtkyphjytpof:pjoiqaj;ew"))
    print(f"{x=}")


def ex2():
    """pprint - 組み込み方やユーザ定義型を分かりやすく表示する

    pprint = pretty printer
    """

    import pprint

    t = [
        [
            [["black", "cyan"], "white", ["green", "red"]],
            [["magenta", "yellow"], "blue"],
        ]
    ]
    pprint.pprint(t, width=30)


def ex3():
    """textwrap - 段落で構成された文章を指定したスクリーン幅にぴったり治める"""
    import textwrap

    doc = """aoiefaeowaoe;aofmaoewifaowieuiweo;wevnoaasdfsd;vm;asssdoifuodfu;oavfu;aoeifuo;aivefmoasdf"""

    print(textwrap.fill(doc, width=40))


def ex4():
    """locale - 文化により異なる形式のデータベースにアクセスする"""
    import locale

    # これは何？
    locale.setlocale(locale.LC_ALL, "English_United States.1252")

    conv = locale.localeconv()  # convention の mapping を取得
    x = 1234567.8
    print(locale.format_string("%d", x, grouping=True))
    print(
        locale.format_string(
            "%s%.*f", (conv["currency_symbol"], conv["frac_digits"], x), grouping=True
        )
    )


def ex5():
    """文字列テンプレート"""
    from string import Template

    # テンプレート
    # 「$」の後ろに識別子を置くことでプレースホルダとなる
    # 「$$」でエスケープ可能
    t = Template("${village}folk send $$10 to $cause")

    print(t.substitute(village="Nottingham", cause="the ditch fund"))


def ex6():
    """struct - バイナリデータの操作"""
    # めんどくさ


def ex7():
    """threading - マルチスレッディング"""
    # めんどくさ


def ex8():
    """logging - ログ記録"""
    import logging

    logging.debug("デバッグ情報")
    logging.info("雑多な情報")
    logging.warning("警告メッセージ")
    logging.error("エラーメッセージ")
    logging.critical("致命的なエラー")


def ex9():
    """weakref - 弱参照"""
    # めんどくさ


def ex10():
    """array - 配列

    同種のデータのみをよりコンパクトに格納する
    """

    from array import array

    a = array("H", [4000, 10, 720, 22222])
    print(sum(a))
    print(a[1:3])


def ex11():
    """collections.deque - キューとして優秀"""
    from collections import deque

    d: deque[str] = deque(["task1", "task2", "task3"])
    # 要素の右からの追加
    d.append("task4")
    # 要素の左からの pop
    print("Handling", d.popleft())


def ex12():
    """bisect - ソート炭のリストを操作する"""
    import bisect

    scores = [(100, "perl"), (200, "tcl"), (300, "lua"), (500, "python")]
    bisect.insort(scores, (400, "ruby"))
    print(scores)


def ex13():
    """heapw - 通常のリストでヒープを実装する

    ヒープでは、もっとも小さい値を持つエントリが常にゼロの位置にある
    """
    from heapq import heapify, heappop, heappush

    data = [4, 6, 4, 23, 2, 4, 6, 7, 7, 4, 2, 2, 0]

    heapify(data)
    print(data)

    heappush(data, -5)
    print(data)

    print([heappop(data) for i in range(3)])

    print(data)


def ex14():
    """decimal - 10進浮動小数演算

    精度の制御が可能"""

    from decimal import Decimal

    print(f"{round(Decimal("0.70") * Decimal("1.05"), 2)=}")

    print(f"{round(.70*1.05,2)=}")


if __name__ == "__main__":
    ex14()

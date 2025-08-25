"""10. 標準ライブラリミニツアー"""

from argparse import Namespace
from datetime import timedelta


def ex1():
    """os"""

    import os

    # cwd = current working directory
    print(f"{os.getcwd()=}")

    # change cwd
    os.chdir("C:\\Users\\M.Endo\\projects\\python-tutorial")
    print(f"{os.getcwd()=}")

    # システムシェルでコマンドを実行
    os.system("mkdir today")


def ex2():
    """shutil

    Shell Utilities
    ファイルやディレクトリの管理"""

    import shutil

    # 関数名は体を表す
    shutil.copyfile("data.db", "archive.db")
    shutil.move("/build/executables", "installdir")


def ex3():
    """glob

    glob = 「かたまり」
    ディレクトリのワイルドカード検索からファイルのリストを生成する"""

    import glob

    print(f"{glob.glob("*.py")=}")


def ex4():
    """コマンドライン引数とそのパース"""
    import sys

    print(sys.argv)

    # コマンドライン引数を処理するべんりなstdlib
    import argparse

    parser = argparse.ArgumentParser(
        prog="std_lib_10",  # 　プログラム名
        description="各ファイルの1行目を表示する",  # 説明
    )

    parser.add_argument("filenames", nargs="+")
    parser.add_argument("-l", "--lines", type=int, default=10)
    args: Namespace = parser.parse_args()
    print(args)


def ex5():
    """stdoutはテキストファイルにしたいけどエラーはシェルに表示したい場合に便利"""
    import sys

    sys.stderr.write("だめ")


def ex6():
    """re

    re = regular expression
    高度な文字列処理"""
    import re

    x = re.findall(r"\b f[a-z]*", "which foot or hand fell fastest")
    print(x)

    y = re.sub(r"(\b[a-z]) \1", r"\1", "cat in the the hat")
    print(y)
    # よくわからない


def ex7():
    """random"""

    import random

    print(f"{random.choice(["apple", "pear", "banana"])=}")
    print(f"{random.sample(range(100), 10)=}")
    print(f"{random.randrange(6)}")  # range(6)から整数をランダムに選ぶ


def ex8():
    """statistics"""
    import statistics
    import random

    data = random.sample(range(100), 10)
    print(f"{data=}")
    print(f"{statistics.mean(data)=}")
    print(f"{statistics.median(data)=}")
    print(f"{statistics.variance(data)=}")


def ex9() -> None:
    """インターネットへのアクセス"""
    from urllib.request import urlopen

    with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
        for line in response:
            line = line.decode()  # str を bytes に変換
            if line.startswith("datetime"):
                print(line.rstrip())


def ex10():
    """メールを送る"""
    import smtplib

    server = smtplib.SMTP("localhost")
    server.sendmail(
        "sample@sample.com",
        "sample@sample.com",
        """To: sample@sample.com
        From sample@sample.com

        aiueo
        """,
    )
    server.quit()
    # ローカルホストでメールサーバーが動いている必要がある
    # よくわからない


def ex11():
    """datetime - 日付と時刻"""

    from datetime import date

    now = date.today()
    print(f"{now=}")
    print(f"{now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")}")

    birthday = date(1920, 8, 5)
    age: timedelta = now - birthday
    print(f"{age=}")


def ex12():
    """データ圧縮"""
    import zlib

    s = b"witch which has which witches wrist watch"
    print(f"{len(s)=}")
    t = zlib.compress(s)
    print(f"{len(t)=}")
    u = zlib.decompress(t)
    print(f"{u=}")


def ex13():
    """パフォーマンスの計測"""
    from timeit import Timer

    # 変数の swap にかかる時間

    print(f"{Timer("t=a;a=b;b=t","a=1;b=2").timeit()}")

    print(f"{Timer("a,b=b,a","a=1;b=2").timeit()}")


def ex14():
    """dectest - 品質管理

    開発と同時にテストを書き、開発の過程で頻繁にテストを走らせる
    """

    # この関数をテストしたい
    def average(values):
        """数値のリストの算術平均の計算
        unittest というのもある

        >>> print(average([20,70,30]))
        40.0
        """

        return sum(values) / len(values)

    import doctest

    doctest.testmod()


if __name__ == "__main__":
    ex14()

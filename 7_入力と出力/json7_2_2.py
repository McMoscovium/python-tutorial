"""7.2.2. jsonによる構造化されたデータの保存

jsonモジュールによるシリアライズ"""

import json


def ex1() -> None:
    """リストからJSON形式の文字列表現を得る"""
    x = [1, "simple", "list"]

    # JSON形式の文字列表現
    print(json.dumps(x))


def ex2() -> None:
    """リストを、JSON形式でtextファイルに書き出す"""
    x = [1, "simple", "list"]
    with open("json_sample.txt", mode="w", encoding="utf-8") as f:
        json.dump(x, f)


def ex3():
    """読み込み用に開かれたファイルをデシリアライズする"""
    with open("json_sample.txt", encoding="utf-8") as f:
        x = json.load(f)
        print(x)


if __name__ == "__main__":
    ex3()

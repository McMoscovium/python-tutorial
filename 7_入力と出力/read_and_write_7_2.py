"""7.2. ファイルを読み書きする"""

from os import SEEK_END


def ex1() -> None:
    """ファイルの読み込み"""
    with open("sample.txt", encoding="utf-8") as f:
        # 何らかの処理
        pass
    # リソースは自動で解放される

    print(f"f.closed : {f.closed}")


def ex2() -> None:
    """1行ずつ読みこむ"""
    with open("sample.txt", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())


def ex3() -> None:
    """ループを使って1行ずつ読む"""
    with open("sample.txt", encoding="utf-8") as f:
        for line in f:
            print(line, end="")


def ex4():
    """ファイルの全ての行をリストにする"""
    with open("sample.txt", encoding="utf-8") as f:
        # リストに行ごとに格納
        print(list(f))

    with open("sample.txt", encoding="utf-8") as f:
        # これでもよい
        print(f.readlines())


def ex5() -> None:
    """書き込み"""
    with open("sample.txt", encoding="utf-8", mode="a") as f:
        # ファイルの現在位置（この場合は先頭）に書き込む
        # 書き込まれた文字数を返す
        print(f.write("テスト文字列\n"))


def ex6():
    """ファイルオブジェクトの位置を変更する"""
    with open("sample.txt", encoding="utf-8") as f:
        # 先頭から0文字目
        print(f.seek(0))
        # 先頭から1文字目に移動する
        print(f.seek(1))
        # ファイルオブジェクトの位置から0文字目に移動する（何もしない関数）
        print(f.seek(0, 1))
        # 末尾に移動する
        print(f.seek(0, SEEK_END))

        # テキストモードの場合、SEEK_CUR=1やSEEK_END=2を基準にしたオフセットは0以外許されない
        # f.seek(1, 1)  # エラー
        # f.seek(-2, 2) # エラー

        # fの現在位置
        print(f.tell())


if __name__ == "__main__":
    ex6()

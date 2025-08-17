# コンテキストマネージャの例


# ジェネレータとしてコンテキストマネージャ―を実装する例
# ジェネレータとは generator iterator を返す関数のこと。
# contextlib.contextmanager デコレータを用いる。
from contextlib import contextmanager


@contextmanager
def contextManagerExample():
    resource = "リソース"  # 扱いたいresourceを準備
    try:
        yield resource  # 準備したresourceを外部に渡す
    finally:
        print("コンテキストマネージャがリソースを解放しました\n")


def main() -> None:
    with contextManagerExample() as r:
        print(r)


# main関数と同じ挙動
def main2() -> None:
    resource = "リソース"  # リソースの準備
    try:
        r = resource  # yield された resource を r という名前で扱う
        print(r)  # 何らかの操作をrについて行う
    finally:
        print(
            "コンテキストマネージャがリソースを解放しました\n"
        )  # resource の cleanup （ここでは単に標準出力に出力）


if __name__ == "__main__":
    main()

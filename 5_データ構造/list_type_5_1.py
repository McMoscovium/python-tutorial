"""5.1 リスト型についてもう少し
https://docs.python.org/ja/3.13/tutorial/datastructures.html#more-on-lists"""

"""
* listクラスのメソッドすべての挙動をインタラクティブモードで確認した。
* x=[0,1,2]のとき、x.pop(2)=2であり、x=[0,1]に変化する。
"""


"""5.1.1 リストをスタックとして使う"""


def ex1():
    """リストはスタックとして使える

    append(), pop()を用いればスタックとして使える。"""
    stack = [3, 4, 5]
    # 末尾に追加
    stack.append(6)
    # 末尾を削除
    stack.pop()  # [3,4,5,6]
    stack.pop()  # [3,4,5]
    stack.pop()  # [3,4]
    stack.pop()  # [3]
    stack.pop()  # []
    stack.pop()  # エラー


"""5.1.2 リストをキューとして使う

最初に追加した要素を最初に取り出す。"""


def ex2() -> None:
    # キューの実装にお勧めのコンテナデータ型
    from collections import deque

    queue: deque[str] = deque(["Amaya", "Bakabon", "Chunichi"])
    queue.append("Dragons")
    queue.popleft()  # "Amaya"
    queue.popleft()  # "Bakabon"
    print(queue)  # deque(["Chunichi", "Dragons"])


if __name__ == "__main__":
    ex2()

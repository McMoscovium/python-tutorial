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


"""5.1.3 リストの内包表記

集合論でよく使う内包表記を用いてリストを生成できる"""


def ex3():
    # 集合の記号を用いると、 { x**2 | x \in range(10) } ただしリストなので順序もデータに含まれる。
    # どちらも [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    squares: list[int] = list(map(lambda x: x**2, range(10)))
    squares2: list[int] = [x**2 for x in range(10)]

    # { (x, y) | x∈[1, 2, 3], y∈[3, 1, 4] with x≠y }
    diff: list[tuple[int, int]] = [
        (x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y
    ]


"""5.1.4. ネストしたリストの内包表記"""


def ex4() -> None:
    # 次のリストに操作をしたい：
    m: list[list[int]] = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # 転置
    t: list[list[int]] = [[row[i] for row in m] for i in range(4)]
    print(t)


if __name__ == "__main__":
    ex4()

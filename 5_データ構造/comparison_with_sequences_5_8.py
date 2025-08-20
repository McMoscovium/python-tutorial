"""5.8. シーケンスとその他の型の比較

https://docs.python.org/ja/3.13/tutorial/datastructures.html#comparing-sequences-and-other-types
"""


# シーケンス型のオブジェクトは、辞書式順序を通してほかのシーケンス型オブジェクトと比較できる。
# しかし、型が異なる時点でinequalとなる
def ex1():
    l = [1, 2, 3, 4, 5]
    d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    print(l == d)


# 異なる型のシーケンスオブジェクトの大小比較はTypeErrorを返す
def ex2():
    l = [1, 2]
    t = (1, 3)
    # print(l < t) # エラー


if __name__ == "__main__":
    ex1()

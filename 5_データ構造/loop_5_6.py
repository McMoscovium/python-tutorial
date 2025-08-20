"""5.6. ループのテクニック

https://docs.python.org/ja/3.13/tutorial/datastructures.html#looping-techniques"""


def ex1():
    """items()メソッドによる辞書の値の列挙"""
    d = dict(a=1, b=2)

    # items()メソッドによるペアの列挙
    print(d.items())
    # dict_items([('a', 1), ('b', 2)])

    for k, v in d.items():
        print(k, v)

    l = [1, 2, 3]
    # 辞書型特有のメソッドなので、リストにitems()メソッドはない。
    # print(l.items())


def ex2():
    """一般のシーケンスの要素の列挙"""

    # 辞書の場合
    d = {"a": 1, "b": 2}
    # enumerateの返り値は（おそらく）イテレータである
    print(list(enumerate(d)))
    # <enumerate object at 0x0000018E7A99ADE0>
    for i, v in enumerate(d):
        print(i, v)
    # 0 a
    # 1 b

    # リストの場合
    l = ["a", "b", "c", "d"]
    for i, v in enumerate(l):
        print(i, v)
    # 0 a
    # 1 b
    # 2 c
    # 3 d


def ex3():
    """2つ以上のシーケンスを同時にループするときに、zip()関数を使える。"""
    names = ["taro", "chimpo", "dragons"]
    ages = [25, 15, 100]
    props = ["strong", "huge", "funny"]
    for name, age, prop in zip(names, ages, props):
        print("{0}({1}) is {2}.".format(name, age, prop))


def ex4():
    """シーケンスを逆向きにループする"""
    it = range(1, 10, 2)
    print(list(it))
    print(list(reversed(it)))
    for i in reversed(it):
        print(i)


def ex5():
    """シーケンスをソートされた形でループする方法"""
    l = [5, 4, 7, 3, 1, 2, 6]
    for i in sorted(l):
        print(i)


def ex6():
    """重複要素の除去"""
    l = [1, 4, 7, 6, 4, 2, 2, 1]
    for i in set(l):
        print(i)
    # 1 2 4 6 7
    # 勝手にソートされている

    print(type(set(l)))  # <class 'set'>


if __name__ == "__main__":
    ex6()

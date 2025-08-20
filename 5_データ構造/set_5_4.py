"""5.4. 集合型"""


def ex():
    s = {1, 2, 3, 4, 1, 2, 4, 6}
    print("s =", s)
    # {1, 2, 3, 4, 6}

    t = {2, 3, 5, 7}
    print("t =", t)

    # 要素が入っているか
    print(4 in s)
    print(4 in t)

    # 差集合
    print("s-t=", s - t)
    # 和集合
    print("s|t=", s | t)
    # 共通部分
    print("s&t=", s & t)
    # 対称差
    print("s^t=", s ^ t)

    # setの内包的定義
    u = {x for x in s if x not in t}
    # これはs - tと同じ
    print("{x for x in s if x not in t}=", u)


if __name__ == "__main__":
    ex()

"""5.2. del文

リストの要素を削除する。
pop()は値を返すが、delは値を返さない
popはlistのメソッドだが、delは違う。"""


def ex() -> None:
    a: list[int] = [0, 1, 2, 3]

    # a.pop(0)
    del a[0]
    # 値を返さない

    del a[:]
    # a=[]

    del a
    # aに何かを代入するまでは、aを参照するとエラーになる

    # print(a == True)  # UnboundLocalError


if __name__ == "__main__":
    ex()

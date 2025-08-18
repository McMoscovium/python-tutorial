"""
キーワード引数
https://docs.python.org/ja/3.13/tutorial/controlflow.html#keyword-arguments
"""


# 長さが不定のタプルや辞書を受け取る場合
# 必ずタプルを先に受け取る
def ex1():
    def f(n, *tuple, **dict):
        print("必須引数 n は ", n)
        print("-------------------")

        print("*tuple は")
        for arg in tuple:
            print(arg)
        print("-------------------")

        print("**dict は")
        for item in dict:
            print(item, ":", dict[item])

        print("\n")

    # 基本的な引数の渡し方
    f(1, 1, 2, 3, name="taro", timpo="huge")

    # タプルや辞書をそのままの形で渡せる
    f(2, *(5, 6, 7), **{"name": "taro", "timpo": "huge"})


if __name__ == "__main__":
    ex1()

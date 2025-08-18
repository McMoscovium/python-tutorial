"""
4.9.8. 関数のアノテーション
https://docs.python.org/ja/3.13/tutorial/controlflow.html#function-annotations
アノテーションは完全にオプショナルらしい
"""


def ex1():
    def f(n, m: int, name: str = "aiueo") -> str:
        """Returns name."""
        return "aiueo"

    # n にはアノテーションがない
    print(f.__annotations__)


if __name__ == "__main__":
    ex1()

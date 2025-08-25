"""9.5. 継承"""


def ex1():
    """名前マングリング"""

    class Mapping:
        def __init__(self, iterable) -> None:
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update

    class MappingSubclass(Mapping):
        def update(self, keys, values):
            # update() への新シグネチャ導入
            # しかし __init__() は壊さない
            for item in zip(keys, values):
                self.items_list.append(item)


from dataclasses import dataclass


def ex2():
    @dataclass
    class Employee:
        name: str
        dept: str
        salary: int

    john = Employee("john", "computer lab", 1000)
    print(f"{john.dept=}")

    mike = Employee("mike", "sales", 2000)
    print(f"{mike.dept=}")

    print(f"{john.dept=}")


if __name__ == "__main__":
    ex2()

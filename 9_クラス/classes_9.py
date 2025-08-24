class MyClass:
    def new_var(aiuie) -> None:
        aiuie.a = 0


x = MyClass()
print(f"{x.__dict__=}")
x.new_var()
print(f"{x.__dict__=}")

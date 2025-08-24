"""8. 例外を処理する"""


def ex1() -> None:
    """例外処理の例"""
    while True:
        try:
            x = int(input("数字を入力してね: "))
            print("数字をありがとう！")
            break
        except ValueError:
            print("それは不適当な数字だよ。もう一度入力してね...")


def ex2() -> None:
    """派生クラスの例外について"""

    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")


def ex3() -> None:
    """引数を持つ例外"""
    try:
        raise Exception("spam", "eggs")
    except Exception as inst:
        print(type(inst))  # 例外の型
        print(inst.args)
        print(inst)  # Exception型は__str__メソッドを持つのでargsを直接printできる
        x, y = inst.args


def ex4() -> None:
    import sys

    try:
        f = open("myfile.txt")
    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=},{type(err)=}")
        raise
    else:
        s = f.readline()
        i = int(s.strip())
        print(f"{i=}")
        f.close()


def this_fails():
    x = 1 / 0


def ex5():
    """raiseによる再送出"""

    def ex5_a():
        print("--- ex5() を実行 ---")
        try:
            this_fails()
        except ZeroDivisionError as err:
            print(
                "例外を捕捉しました:",
                err,
            )
            raise

    try:
        ex5()
    except ZeroDivisionError:
        print("\n--- ex5() からの例外が上位で捕捉されました ---")
        print("トレースバック:")
        import traceback

        traceback.print_exc()


def ex6():
    """raise errで再送出した場合

    変わらない😡"""

    def ex6_a():
        """try節で呼び出された関数の例外を捕捉し、raise errで再送出する"""
        print("--- ex6_a() を実行 ---")
        try:
            this_fails()
        except ZeroDivisionError as err:
            print("例外を捕捉しました:", err)
            # 新しい例外として再送出するため、元のトレースバックは失われる
            raise err

    try:
        ex6_a()
    except ZeroDivisionError:
        print("\n--- ex6_a() からの例外が上位で捕捉されました ---")
        # トレースバックを確認
        print("トレースバック:")
        import traceback

        traceback.print_exc()


def ex7() -> None:
    """例外の送出"""

    # 例外クラスのインスタンスでなくても、クラスのみ渡すと引数無しのコンストラクタを実行した結果が送出される。
    try:
        raise Exception  # raise Exception() と同じ
    except Exception:
        pass


def ex8():
    """クリーンアップ動作 finally

    単純な例"""
    try:
        raise Exception
    except Exception:
        print("例外を処理")
    finally:
        print("finally処理")


def ex9():
    """try節で送出された例外が捕捉されなかった場合"""
    try:
        raise Exception
    except ValueError:
        # これはExceptionを補足しない
        print("例外処理")
    finally:
        print("finally 処理")
        # Exceptionを再送出する


def ex10():
    """except 節やで例外が送出された場合"""
    try:
        raise Exception("err1")
    except Exception as err1:
        print(f"{err1}", "を例外処理")
        raise Exception("err2")
    finally:
        print("finally 処理")
        # err2 を再送出


def ex11() -> None:
    """else 節で例外が送出された場合"""
    try:
        pass
    except:
        pass
    else:
        print("else 節")
        raise Exception
    finally:
        print("finally 節")
        # Exceptionを再送出


def ex12() -> str:
    """しかし finally 節が break, continue, return を実行する場合、再送出は行われない。"""
    try:
        raise Exception
    except ValueError:
        # これはExceptionを補足しない
        print("例外処理")
    finally:
        return str("finally の返り値")
        # 再送出は行われない


def ex13() -> str | None:
    """try 節でbreak, continue, return をに到達すると、その直前にfinallyを実行する"""
    try:
        return str("try の返り値")
    except:
        pass
    else:
        print("これは実行されないはず")
    finally:
        print("finally 実行")


def ex14() -> str:
    """finally 節で return に達すると、返り値は try のものではなく finally のものになる"""
    try:
        return str("これは返らないはず")
    except:
        pass
    else:
        print("ここには到達しない")
    finally:
        return str("finally 返り値")


def ex15() -> None:
    """ExceptionGroup : 互いに無関係な複数の例外をまとめて送出する

    並列処理などでは頻繁に使うし、ほかの場面でも例外発生時に処理を継続したい場合がある"""

    def f():
        excs = [OSError("error 1"), SystemError("error 2")]
        raise ExceptionGroup("there were problems", excs)

    try:
        f()
    except Exception as e:
        print(f"caught {type(e)}: e")


def ex16():
    """ExceptionGroup から特定の例外を取り出す"""

    def f():
        raise ExceptionGroup(
            "group1",
            [
                OSError(1),
                SystemError(2),
                ExceptionGroup("group2", [OSError(3), RecursionError(4)]),
            ],
        )

    try:
        f()
    except* OSError as e:
        print("OSError", f"{e}", "を捕捉")
    except* SystemError as e:
        print("SystemError", f"{e}", "を捕捉")


def ex17():
    """ExceptionGroup を作成する"""
    excs = []
    for i in range(3):
        try:
            1 / 0
        except Exception as e:
            excs.append(e)
    if excs:
        raise ExceptionGroup("エラー達", excs)


def ex18():
    """例外にノートを加える"""
    try:
        raise TypeError("バカ型")
    except Exception as e:
        e.add_note("これはバカ型だよ")
        e.add_note("誰ですかこれ作ったの")
        raise


if __name__ == "__main__":
    ex18()

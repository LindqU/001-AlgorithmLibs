"""hogehoge"""
from utility.mock_std import In, Out


def test_mock_input():
    file_path = "tests/utility/test1.txt"
    stdin = In(file_path)

    res = list()
    first_row = stdin.pop()
    res.append(first_row)
    for _ in range(int(first_row)):
        res.append(stdin.pop())
    assert res == ["4", "1 4", "4 3", "4 10", "8 3"]


def test_mock_out1():
    """正常系1
    通常ケース
    """
    file_path = "tests/utility/test1.txt"

    stdout = Out(file_path)
    stdout.add("4")
    stdout.add("1 4")
    stdout.add("4 3")
    stdout.add("4 10")
    stdout.add("8 3")
    assert stdout.validation == stdout.outputs


def test_mock_out2():
    """print(1, 6) パターン issue#6"""
    file_path = "tests/utility/test2.txt"
    stdout = Out(file_path)
    stdout.add("1")
    stdout.add(" ")
    stdout.add("60")
    assert stdout.validation == stdout.outputs

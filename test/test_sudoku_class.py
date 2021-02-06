"""
数独类的测试模块

该模块用于测试sudoku.sudoku_class模块的单元测试

:copyright: (c) 2021 by 李浚哲.
"""

import operator
from sudoku.sudoku_class import Sudoku

# 9*9
matrix1 = [[4, 7, 3, 5, 1, 8, 6, 9, 2],
           [9, 2, 8, 6, 3, 4, 5, 1, 7],
           [5, 6, 1, 7, 2, 9, 3, 4, 8],
           [6, 4, 2, 8, 7, 1, 9, 5, 3],
           [1, 8, 7, 9, 5, 3, 4, 2, 6],
           [3, 9, 5, 2, 4, 6, 7, 8, 1],
           [7, 1, 6, 4, 9, 2, 8, 3, 5],
           [2, 5, 9, 3, 8, 7, 1, 6, 4],
           [8, 3, 4, 1, 6, 5, 2, 7, 9]]
# 8*9
matrix2 = [[4, 7, 3, 5, 1, 8, 6, 9, 2],
           [9, 2, 8, 6, 3, 4, 5, 1, 7],
           [5, 6, 1, 7, 2, 9, 3, 4, 8],
           [6, 4, 2, 8, 7, 1, 9, 5, 3],
           [1, 8, 7, 9, 5, 3, 4, 2, 6],
           [3, 9, 5, 2, 4, 6, 7, 8, 1],
           [7, 1, 6, 4, 9, 2, 8, 3, 5],
           [2, 5, 9, 3, 8, 7, 1, 6, 4]]
# 9*8
matrix3 = [[4, 7, 3, 5, 1, 8, 6, 9],
           [9, 2, 8, 6, 3, 4, 5, 1],
           [5, 6, 1, 7, 2, 9, 3, 4],
           [6, 4, 2, 8, 7, 1, 9, 5],
           [1, 8, 7, 9, 5, 3, 4, 2],
           [3, 9, 5, 2, 4, 6, 7, 8],
           [7, 1, 6, 4, 9, 2, 8, 3],
           [2, 5, 9, 3, 8, 7, 1, 6],
           [8, 3, 4, 1, 6, 5, 2, 7]]

# 9*9problem
matrix4 = [[0, 0, 0, 0, 0, 5, 0, 2, 0],
           [1, 0, 0, 9, 0, 0, 0, 0, 0],
           [4, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 8, 0, 0, 2, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 9, 0, 4],
           [0, 0, 5, 0, 0, 0, 3, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 7],
           [0, 0, 2, 4, 0, 8, 0, 0, 0]]

# 9*9
matrix5 = [[4, 7, 3, 5, 4, 8, 6, 9, 2],
           [9, 2, 8, 6, 3, 4, 5, 1, 7],
           [5, 6, 1, 7, 2, 9, 3, 4, 8],
           [6, 4, 2, 8, 7, 1, 9, 5, 3],
           [1, 8, 7, 9, 5, 3, 4, 2, 6],
           [3, 9, 5, 2, 4, 6, 7, 8, 1],
           [7, 1, 6, 4, 9, 2, 8, 3, 5],
           [2, 5, 9, 3, 8, 7, 1, 6, 4],
           [8, 3, 4, 1, 6, 5, 2, 7, 9]]

s = Sudoku()


def test_load():
    """
    测试load方法加载一个数独
    """
    assert s.load(matrix1) is True
    assert s.load(matrix2) is False
    assert s.load(matrix3) is False


def test_get():
    """
    测试get方法获取数独
    """
    assert operator.eq(matrix1, s.get()) is True


def test_is_valid():
    """
    测试当前的数独是否填写完整且正确
    """
    assert s.is_valid() is True
    assert s.load(matrix5) is True
    assert s.is_valid() is False
    assert s.load(matrix4) is True
    assert s.is_valid() is False


def test_write_to_file():
    """
    测试文件写入
    """
    with open('test.txt', 'w') as outfile:
        s.write_to_file(outfile)


def test_load_from_file():
    """
    测试从文件读取数独
    """
    with open('test.txt', 'r') as infile:
        s.load_from_file(infile)


def test_solve():
    """
    测试求解数独
    """
    s.solve()
    assert s.is_valid() is True


def test_solve_from_file():
    """
    测试求解文件中的数独
    """
    s.solve_from_file('games.txt')

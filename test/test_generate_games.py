"""
生成数独开局的测试模块

该模块用于测试sudoku.generate_games模块的单元测试

:copyright: (c) 2021 by 李浚哲.
"""

import operator
from sudoku.generate_games import GenerateGames

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

g = GenerateGames()


def test_load():
    """
    测试load方法加载一个数独
    """
    assert g.load(matrix1) is True
    assert g.load(matrix2) is False
    assert g.load(matrix3) is False


def test_get():
    """
    测试get方法获取数独
    """
    assert operator.eq(matrix1, g.get()) is True


def test_dig():
    """
    测试挖空
    """
    g.dig()


def test_write_to_file():
    """
    测试文件写入
    """
    with open('test.txt', 'w') as outfile:
        g.write_to_file(outfile)


def test_generate():
    """
    测试批量生成数独开局
    """
    g.generate('endgames.txt', 'games.txt')

"""
生成数独终局的测试模块

该模块用于测试sudoku.generate_endgames模块的单元测试

:copyright: (c) 2021 by 李浚哲.
"""

import operator
from sudoku.generate_endgames import GenerateEndgames

g = GenerateEndgames()


def test_generate():
    """
    测试generate方法
    """
    # 测试number参数
    assert g.generate(0, 10, 'test.txt') is False
    assert g.generate(1, 10, 'test.txt') is True
    assert g.generate(9, 10, 'test.txt') is True
    assert g.generate(10, 10, 'test.txt') is False
    assert g.generate(1.5, 10, 'test.txt') is False
    assert g.generate('1', 10, 'test.txt') is False
    # 测试quantity参数
    assert g.generate(5, 0, 'test.txt') is False
    assert g.generate(5, 1, 'test.txt') is True
    assert g.generate(5, 1000, 'endgames.txt') is True
    assert g.generate(5, 1.5, 'test.txt') is False
    assert g.generate(5, '1', 'test.txt') is False


def test_generate_one():
    """
    测试generate_one方法
    """
    g.generate_one()


def test_write_to_file():
    """
    测试文件写入
    """
    with open('test.txt', 'w') as outfile:
        g.write_to_file(outfile)


def test_get():
    """
    测试get方法
    """
    # 从输出的文件中读取数独
    with open('test.txt', 'r') as infile:
        lines = infile.readlines()
        matrix = []
        for line in lines:
            matrix.append(list(map(int, line.rstrip('\n').split(' '))))
    # 判断文件中的数独是否和get方法获得的数独一致
    assert operator.eq(matrix, g.get()) is True

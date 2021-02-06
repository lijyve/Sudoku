"""
生成游戏模块

这个模块实现了生成数独开局的功能类

:copyright: (c) 2021 by 李浚哲.
"""

import random
from copy import deepcopy


class GenerateGames:
    """
    生成数独开局的功能类
    1.可以调用generate方法将输入文件中的数独终局批量地生成数独开局
    2.调用load方法加载一个数独终局,调用dig方法对当前数独随机挖空,调用get方法获得数独开局
    """

    def __init__(self):
        self.__matrix = []

    def load(self, matrix):
        """
        加载一个矩阵作为数独
        :param matrix: 9*9的二维数组
        :return: True正确加载, False输入矩阵格式错误
        """
        if len(matrix) != 9:
            return False
        for row in matrix:
            if len(row) != 9:
                return False
        self.__matrix = deepcopy(matrix)
        return True

    def get(self):
        """
        获取当前数独
        :return: list[list[int]]类型的变量,为当前数独终局的引用
        """
        return self.__matrix

    def write_to_file(self, out):
        """
        将数独写入文件
        :param out: 输出文件描述符
        :return:
        """
        for i in range(8):
            row = str(self.__matrix[i])[1:-1].replace(',', '') + '\n'
            out.write(row)
        out.write(str(self.__matrix[-1])[1:-1].replace(',', ''))

    def dig(self):
        """
        将数独终局挖空，生成数独题目
        :return:
        """
        # 每个3×3小棋盘挖空2个
        for i in range(9):
            grid_x = int(i / 3)
            grid_y = i % 3
            random_index = random.sample(range(0, 9), 2)
            for j in range(2):
                row = grid_x * 3 + int(random_index[j] / 3)
                column = grid_y * 3 + random_index[j] % 3
                self.__matrix[row][column] = 0
        # 将非零的空放入数据集
        samples = [(x, y) for x in range(0, 9) for y in range(0, 9) if self.__matrix[x][y] != 0]
        # 生成采样数量
        sampling_number = random.randint(12, 42)
        # 从数据集中采样并挖空
        holes = random.sample(samples, sampling_number)
        for row, column in holes:
            self.__matrix[row][column] = 0

    def generate(self, infile='sudoku.txt', outfile='sudoku_games.txt'):
        """
        批量生成数独开局
        :param infile: 保存数独终局的文件名
        :param outfile: 输出数独开局的文件名
        :return:
        """
        self.__matrix.clear()
        with open(infile, 'r') as file1:
            lines = file1.readlines()
            with open(outfile, 'w') as file2:
                for line in lines:
                    if line == '\n':
                        self.dig()
                        self.write_to_file(file2)
                        file2.write('\n\n')
                        self.__matrix.clear()
                    else:
                        # 将输入的一行字符串转换成一维整型列表并插入数独矩阵
                        self.__matrix.append(list(map(int, line.rstrip('\n').split(' '))))
                self.dig()
                self.write_to_file(file2)

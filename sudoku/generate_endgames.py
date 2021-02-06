"""
生成游戏终局模块

这个模块实现了生成数独终局的功能类

:copyright: (c) 2021 by 李浚哲.
"""

import random
from itertools import permutations
from copy import deepcopy


class GenerateEndgames:
    """
    生成数独终局的功能类
    1.可以调用generate方法批量生成数独终局并输出至文件
    2.可以调用generate_one方法随机生成一个数独终局,结果可以通过get方法获得
    """

    def __init__(self):
        self.__offset = [0, 3, 6, 1, 4, 7, 2, 5, 8]
        self.__swap_first_rows = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        self.__swap_second_rows = [[3, 4, 5], [3, 5, 4], [4, 3, 5], [4, 5, 3], [5, 3, 4], [5, 4, 3]]
        self.__swap_third_rows = [[6, 7, 8], [6, 8, 7], [7, 6, 8], [7, 8, 6], [8, 6, 7], [8, 7, 6]]
        self.__matrix = []
        self.__matrix_swap = []

    def get(self):
        """
        获取当前生成的数独终局
        :return: list[list[int]]类型的变量,为当前数独终局的引用
        """
        return self.__matrix_swap

    def write_to_file(self, out):
        """
        将数独写入文件
        :param out: 输出文件描述符
        :return:
        """
        for i in range(8):
            row = str(self.__matrix_swap[i])[1:-1].replace(',', '') + '\n'
            out.write(row)
        out.write(str(self.__matrix_swap[-1])[1:-1].replace(',', ''))

    def __offset_first_row(self, row0):
        """
        用row0和预置的偏移列表生成一个基础的终局
        :param row0: 第一行
        :return:
        """
        temp_row = deepcopy(row0)
        # 遍历所有偏移量
        for offset in self.__offset:
            # 用当前的偏移量去偏移下一行
            for old_index in range(9):
                new_index = (old_index + offset) % 9  # 计算偏移后的位置
                temp_row[new_index] = row0[old_index]  # 偏移
            self.__matrix.append(deepcopy(temp_row))

    def __swap_rows(self, first, second, third):
        """
        交换行
        :param first: 前三行的交换方法
        :param second: 中间三行的交换方法
        :param third: 最后三行的交换方法
        :return:
        """
        # 交换前三行中的第2,3行
        for i in range(3):
            self.__matrix_swap.append(self.__matrix[self.__swap_first_rows[first][i]])
        # 交换中间三行
        for i in range(3):
            self.__matrix_swap.append(self.__matrix[self.__swap_second_rows[second][i]])
        # 交换后三行
        for i in range(3):
            self.__matrix_swap.append(self.__matrix[self.__swap_third_rows[third][i]])

    def generate(self, number: int, quantity: int, outfile='sudoku.txt'):
        """
        用于批量生成数独终局并输出至文件
        :param number: 终局左上角第一个数字
        :param quantity: 终局数量
        :param outfile: 输出文件路径
        :return: True成功执行, False错误
        """
        # 判断参数合法性
        if not isinstance(number, int) or not isinstance(quantity, int) or \
                number < 1 or number > 9 or quantity < 1:
            return False
        # 清空成员变量
        self.__matrix.clear()
        self.__matrix_swap.clear()
        # 打乱偏移列表
        for i in range(3):
            if i == 0:  # 第一个偏移量0不变,保证第一个数字位置不变
                bias_x = i * 3 + random.randint(1, 2)
                bias_y = i * 3 + random.randint(1, 2)
            else:
                bias_x = i * 3 + random.randint(0, 2)
                bias_y = i * 3 + random.randint(0, 2)
            self.__offset[bias_x], self.__offset[bias_y] = \
                self.__offset[bias_x], self.__offset[bias_y]
        # 生成数独第一行后8位数的全排列
        first_row = [i for i in range(1, 10) if i != number]
        its = permutations(first_row)

        with open(outfile, 'w') as out:
            # 枚举所有的第一行
            for row_it in its:
                row0 = list(row_it)
                row0.insert(0, number)
                # 偏移第一行形成一个基础数独终局
                self.__offset_first_row(row0)
                # 在当前数独终局的基础上枚举所有的交换方式
                for first in range(2):
                    for second in range(6):
                        for third in range(6):
                            self.__swap_rows(first, second, third)
                            # 保存终局到文件
                            self.write_to_file(out)
                            # 记录剩余数独终局个数
                            quantity -= 1
                            if quantity == 0:
                                return True
                            out.write('\n\n')

                            self.__matrix_swap.clear()
                self.__matrix.clear()
        return True

    def generate_one(self):
        """
        没有约束地随机生成一个数独终局
        :return:
        """
        self.__matrix.clear()
        self.__matrix_swap.clear()
        first_row = list(range(1, 10))
        random.shuffle(first_row)
        self.__offset_first_row(first_row)
        self.__swap_rows(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))

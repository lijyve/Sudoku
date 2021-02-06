"""
数独模块

这个模块实现了数独实体类

:copyright: (c) 2021 by 李浚哲.
"""

from copy import deepcopy


class Sudoku:
    """
    数独实体类
    1.可以调用solve_from_file方法批量求解输入文件中的数独题
    2.调用load方法加载一个数独,调用solve方法求解当前数独,调用get方法获得当前数独
    """

    def __init__(self):
        self.__matrix = []
        self.__lines = []

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

    def load_from_file(self, file):
        """
        从文件中加载数独题目
        :param file: 输入文件描述符
        :return:
        """
        self.__lines = file.readlines()

    def get(self):
        """
        获取当前数独
        :return: list[list[int]]类型的变量,为当前数独终局的引用
        """
        return self.__matrix

    def is_valid(self):
        """
        检查数独是否合法
        :return: True合法, False非法
        """
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        palaces = [{} for _ in range(9)]

        for row in range(9):
            for column in range(9):
                palace = (row // 3) * 3 + column // 3
                num = self.__matrix[row][column]
                if num == 0:
                    return False
                rows[row][num] = rows[row].get(num, 0) + 1
                columns[column][num] = columns[column].get(num, 0) + 1
                palaces[palace][num] = palaces[palace].get(num, 0) + 1
                if not (rows[row][num] & 1 and
                        columns[column][num] & 1 and
                        palaces[palace][num] & 1):
                    return False
        return True

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

    def solve(self):
        """
        求解当前的数独题目
        :return:
        """
        rows = [set(range(1, 10)) for _ in range(9)]
        columns = [set(range(1, 10)) for _ in range(9)]
        palaces = [set(range(1, 10)) for _ in range(9)]
        blank = set()

        # 初始化，按照行、列、宫 分别存入哈希表
        for row in range(9):
            for column in range(9):
                number = self.__matrix[row][column]
                if number == 0:
                    blank.add((row, column))
                else:
                    rows[row].remove(number)
                    columns[column].remove(number)
                    palaces[(row // 3) * 3 + column // 3].remove(number)

        # 深搜
        def dfs():
            # 全部填完,回溯
            if len(blank) == 0:
                return True
            max_len = 9
            best_r, best_c, best_p = 0, 0, 0
            # 找到选择最少的空
            for (r_i, c_i) in blank:
                p_i = (r_i // 3) * 3 + c_i // 3
                choices = rows[r_i] & columns[c_i] & palaces[p_i]
                # 如果当前空格可选数字个数小于历史最优
                if len(choices) < max_len:
                    max_len = len(choices)
                    best_r, best_c, best_p = r_i, c_i, p_i
            # 没有选择,已有的选择中存在错误,要回溯
            if max_len == 0:
                return False
            blank.remove((best_r, best_c))
            # 位运算求当前空格的所有可选数字
            choices = rows[best_r] & columns[best_c] & palaces[best_p]
            # 遍历当前空格的所有可选数字
            for num in choices:
                # 填写
                self.__matrix[best_r][best_c] = num
                rows[best_r].remove(num)
                columns[best_c].remove(num)
                palaces[best_p].remove(num)
                # 深搜
                if dfs():
                    return True
                # 删除已填
                rows[best_r].add(num)
                columns[best_c].add(num)
                palaces[best_p].add(num)
            blank.add((best_r, best_c))
            return False

        dfs()

    def solve_from_file(self, input_file, output_file='sudoku.txt'):
        """
        求解input_file中的数独题，并将结果输入到output_file
        :param input_file: 输入文件文件名
        :param output_file: 输出文件文件名
        :return:
        """
        self.__matrix.clear()
        with open(input_file, 'r') as file1:
            self.load_from_file(file1)
            with open(output_file, 'w') as file2:
                for line in self.__lines:
                    if line == '\n':  # 空行
                        self.solve()
                        self.write_to_file(file2)
                        file2.write('\n\n')
                        self.__matrix.clear()
                    else:  # 数独
                        self.__matrix.append(list(map(int, line.rstrip('\n').split(' '))))
                self.solve()
                self.write_to_file(file2)

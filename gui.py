"""
用户图形界面模块

这个模块实现了数独游戏的GUI

:copyright: (c) 2021 by 李浚哲.
"""

from tkinter import Tk, Frame, Button, Menu
from tkinter import NORMAL, DISABLED, RAISED, SUNKEN, GROOVE
from tkinter import StringVar
from tkinter import messagebox
import webbrowser
import os
import base64
from icon import img
from sudoku import *


class Gui:
    """
    用户图形界面类
    """

    def __init__(self):
        self.number = ''
        self.question = []
        self.answer = []
        # 主窗口
        self.root = Tk()
        self.root.title('数独游戏')
        width = 325
        height = 417
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        # 定位到屏幕中央
        self.root.geometry('%dx%d+%d+%d' % (width, height,
                                            (screen_w - width) / 2,
                                            (screen_h - height) / 2))
        # 添加图标
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.root.iconbitmap("tmp.ico")
        self.root.iconbitmap('tmp.ico')
        os.remove("tmp.ico")
        # 菜单栏
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.main_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='主菜单', menu=self.main_menu)
        self.main_menu.add_command(label='在线帮助', command=help_show)
        self.main_menu.add_command(label='关于', command=about_show)

        # 顶部
        self.top = Frame(self.root, highlightbackground='black',
                         highlightcolor='black', highlightthickness=1)
        self.top.grid(row=0, column=0, padx=10, pady=5)
        # 九宫
        self.palaces = [Frame(self.top,
                              highlightbackground='black',
                              highlightcolor='orange',
                              highlightthickness=1) for _ in range(9)]
        for p_idx in range(9):
            p_x = p_idx // 3
            p_y = p_idx % 3
            self.palaces[p_idx].grid(row=p_x, column=p_y)
        # 顶部9*9数独九宫格
        self.grids_num = [[StringVar() for _ in range(9)] for _ in range(9)]
        self.grids = [
            [Button(self.palaces[(row // 3) * 3 + column // 3],
                    width=3, relief=GROOVE,
                    textvariable=self.grids_num[row][column],
                    command=lambda row_i=row, col_i=column: self.grid_click(row_i, col_i))
             for column in range(9)] for row in range(9)]
        # 放置九宫格
        for row in range(9):
            for column in range(9):
                self.grids[row][column].grid(row=row, column=column, padx=1, pady=1)

        # 中部
        self.middle = Frame(self.root)
        self.middle.grid(row=1, column=0, padx=10, pady=5)
        # 中部候选数字
        self.numbers = [Button(self.middle, width=3, text=str(i),
                               command=lambda idx=i: self.num_click(idx))
                        for i in range(1, 10)]
        for column in range(9):
            self.numbers[column].grid(row=0, column=column, padx=1, pady=1)

        # 底部
        self.bottom = Frame(self.root)
        self.bottom.grid(row=2, column=0, padx=10, pady=5)
        # 删除按钮
        self.delete = Button(self.bottom, text='删除', command=self.delete_click,
                             bg='red', fg='white')
        self.delete.grid(row=0, column=0, padx=5, pady=2)
        # 新开局按钮
        self.start = Button(self.bottom, text='新开局', command=self.start_click,
                            bg='blue', fg='white')
        self.start.grid(row=0, column=1, padx=5, pady=2)
        # 自动求解按钮
        self.solve = Button(self.bottom, text='自动求解', command=self.solve_click,
                            bg='orange', fg='white')
        self.solve.grid(row=0, column=2, padx=5, pady=2)
        # 检测按钮
        self.check = Button(self.bottom, text='检查', command=self.check_click,
                            bg='green', fg='white')
        self.check.grid(row=0, column=3, padx=5, pady=2)

        self.root.mainloop()

    def grid_click(self, row, column):
        """
        数独的点击事件
        :param row: 行号
        :param column: 列号
        :return:
        """
        self.grids_num[row][column].set(self.number)

    def num_click(self, num):
        """
        数字的点击事件
        :param num: 数字
        :return:
        """
        # 将所有候选数字和删除键抬起
        for i in range(9):
            self.numbers[i]['relief'] = RAISED
        self.delete['relief'] = RAISED

        # 按下对应数字
        self.numbers[num - 1]['relief'] = SUNKEN
        self.number = num

    def delete_click(self):
        """
        删除按钮的点击事件
        :return:
        """
        # 将所有候选数字抬起
        for i in range(9):
            self.numbers[i]['relief'] = RAISED

        # 按下删除键
        self.delete['relief'] = SUNKEN
        self.number = ''

    def start_click(self):
        """
        开始按钮的点击事件
        :return:
        """
        # 将所有候选数字抬起
        for i in range(9):
            self.numbers[i]['relief'] = RAISED
        self.delete['relief'] = RAISED
        # 生成数独终局
        g_1 = GenerateEndgames()
        g_1.generate_one()
        # 生成数独开局
        g_2 = GenerateGames()
        g_2.load(g_1.get())
        g_2.dig()
        self.question = g_2.get()
        # 填充
        for row in range(9):
            for column in range(9):
                if self.question[row][column] != 0:
                    self.grids_num[row][column].set(self.question[row][column])
                    self.grids[row][column]['stat'] = DISABLED
                else:
                    self.grids_num[row][column].set('')
                    self.grids[row][column]['stat'] = NORMAL

    def solve_click(self):
        """
        自动求解按钮的点击事件
        :return:
        """
        # 求解
        if len(self.question) != 0:
            solver = Sudoku()
            solver.load(self.question)
            solver.solve()
            result = solver.get()
            # 填充
            for row in range(9):
                for column in range(9):
                    self.grids_num[row][column].set(result[row][column])

    def check_click(self):
        """
        检查按钮的点击事件
        :return:
        """
        self.answer.clear()
        for row in range(9):
            temp_row = []
            for column in range(9):
                if self.grids_num[row][column].get() == '':
                    temp_row.append(0)
                else:
                    temp_row.append(int(self.grids_num[row][column].get()))
            self.answer.append(temp_row)
        sudoku = Sudoku()
        sudoku.load(self.answer)
        if sudoku.is_valid():
            messagebox.showinfo(message='恭喜你答对了！')
        else:
            messagebox.showinfo(message='存在错误呢，请仔细检查😄')


def help_show():
    """
    帮助菜单懒的点击事件
    :return:
    """
    # messagebox.showinfo(title='帮助', message='使用教程请查看在线手册.')
    webbrowser.open('https://blog.virsnorlax.com/index.php/archives/6/')


def about_show():
    """
    关于菜单栏的点击事件
    :return:
    """
    messagebox.showinfo(title='关于', message='数独游戏v1.0.0\npower by VirSnorlax.')


if __name__ == '__main__':
    form = Gui()

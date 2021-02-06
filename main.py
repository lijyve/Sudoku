"""
命令行版数独游戏的入口

在命令行输入 'python main.py -h' 查看帮助

:copyright: (c) 2021 by 李浚哲.
"""

import os
import sys
import time
from colorama import init, Fore
from sudoku.generate_endgames import GenerateEndgames
from sudoku.sudoku_class import Sudoku


def option_help():
    """
    帮助
    :return:
    """
    print(Fore.RED + "[Usage]")
    print(Fore.GREEN + '\tpython main.py [-h|--help]')
    print('\t\tList available subcommands and some concept guides.')
    print(Fore.GREEN + '\tpython main.py -c <NUMBER>')
    print('\t\tGenerates <NUMBER> Sudoku endgames,'
          ' NUMBER must be an integer between 1 and 1000000.')
    print(Fore.GREEN + '\tpython main.py -s <TEXT FILE>')
    print('\t\tSolve the Sudoku problem in the file.')
    print()


def main(argv):
    """
    命令行版数独的主函数
    :return:
    """
    init(autoreset=True)
    start_time = time.time()
    parameters = argv
    try:
        if len(parameters) > 3 or len(parameters) < 2:  # 参数个数少于2或多于3
            raise ValueError
        if len(parameters) == 2:  # 参数个数等于2
            if parameters[1] != '-h' and parameters[1] != '--help':  # 参数2不是帮助
                raise ValueError
            option_help()
        else:  # 参数个数等于3
            if parameters[1] == '-c':  # 生成数独终局
                if (not parameters[2].isdigit()) or \
                        (int(parameters[2]) < 1) or \
                        (int(parameters[2]) > 1000000):  # 参数3的数量非法
                    raise ValueError
                generate = GenerateEndgames()
                generate.generate(5, int(parameters[2]))
            elif parameters[1] == '-s':  # 求解数独
                if parameters[2][-4:] != '.txt' or \
                        not os.path.exists(parameters[2]):  # 参数3的输入文件不存在
                    raise IOError
                solver = Sudoku()
                solver.solve_from_file(parameters[2], 'sudoku.txt')
            else:  # 参数2的功能非法
                raise ValueError
    except ValueError:
        print(Fore.RED + '[ERROR] Invalid parameters entered.')
    except IOError:
        print(Fore.RED + '[ERROR] The File name is wrong or failed to read/write file')
    finally:
        print('[INFO] Took ' + str(round((time.time() - start_time), 2)) + ' seconds.')


if __name__ == '__main__':
    main(sys.argv)

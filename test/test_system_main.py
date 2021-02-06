"""
主函数的测试模块

该模块是用于测试main模块的单元测试

:copyright: (c) 2021 by 李浚哲.
"""

import sys
from main import main


def test_main():
    """
    测试main函数对输入指令的处理
    """
    # 备份标准输出
    started_out = sys.stdout
    # 重定位标准输出到文件
    sys.stdout = open('main_out.txt', 'w')

    # python main.py
    main(['main.py'])
    print('-' * 20)
    # python main.py -h
    main(['main.py', '-h'])
    print('-' * 20)
    # python main.py --help
    main(['main.py', '--help'])
    print('-' * 20)
    # python main.py abc
    main(['main.py', 'abc'])
    print('-' * 20)
    # python main.py -c 0
    main(['main.py', '-c', '0'])
    print('-' * 20)
    # python main.py -c 1000001
    main(['main.py', '-c', '1000001'])
    print('-' * 20)
    # python main.py -c 10
    main(['main.py', '-c', '10'])
    print('-' * 20)
    # python main.py -c abc
    main(['main.py', '-c', 'abc'])
    print('-' * 20)
    # python main.py -s games.txt
    main(['main.py', '-s', 'games.txt'])
    print('-' * 20)
    # python main.py -s not_exists.txt
    main(['main.py', '-s', 'not_exists.txt'])
    print('-' * 20)
    # python main.py -s abc
    main(['main.py', '-s', 'abc'])
    print('-' * 20)
    # python main.py -n games.txt
    main(['main.py', '-n', 'games.txt'])
    # python main.py -s games.txt extra_parameter
    main(['main.py', '-s', 'games.txt', 'extra_parameter'])
    # 恢复标准输出
    sys.stdout.close()
    sys.stdout = started_out

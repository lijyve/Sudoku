# Sudoku
软工大作业——数独游戏

看这里 $\longrightarrow$ 博客地址 [数独游戏开发记录](https://virtual-y-monster.gitee.io/) 

# 使用说明

## 环境配置

命令行版数独和图形界面版数独都提供了用 `Pyinstaller` 打包生成的可执行文件，但我仍然 **推荐使用python解释器去运行代码** ，因为在测试过程中，可执行文件sudoku.exe运行会慢于python解释器运行.py文件。这需要你预先配置虚拟环境，我为你提供了两种配置文件 `pip_requirements.txt和conda_requirements.txt` ， 配置方法如下：

如果你用的是pip包管理工具，你可以在创建好的虚拟环境中使用下面这条命令安装必要的包

```
pip install -r pip_requirements.txt
```

如果你用的是conda包管理工具，你可以在创建好的虚拟环境中使用下面这条命令安装必要的包

```
conda install --yes --file conda_requirements.txt
```

## 命令行版数独游戏

有两种执行方式：

### 1. 用python解释器执行（非常推荐！）

1. 创建虚拟环境，根据 `环境配置` 所述安装依赖的包，激活虚拟环境

2. 进入 `Sudoku`  文件夹下

3. 在命令行中输入 `python main.py -h` 或 `python main.py --help` 查看帮助

4. 在命令行中使用-c参数加数字N（1<=N<=1000000）控制生成数独终局的数量，例如下述命令会生成20个数独终局并保存在 `sudoku.txt` 文件中：

   ```
   python main.py -c 20
   ```

5. 在命令行中使用-s参数加文件名的形式求解数独，并将结果输出至 `sudoku.txt` 文件，如：

   ```
   python main.py -s games.txt
   ```

### 2. 执行可执行文件sudoku.exe

3. 在命令行中输入 `.\sudoku.exe -h` 或 `.\sudoku.exe --help` 查看帮助

4. 在命令行中使用-c参数加数字N（1<=N<=1000000）控制生成数独终局的数量，例如下述命令会生成20个数独终局并保存在 `sudoku.txt` 文件中：

   ```
   .\sudoku.exe -c 20
   ```

4. 在命令行中使用-s参数加文件名的形式求解数独，并将结果输出至 `sudoku.txt` 文件，如：

   ```
   .\sudoku.exe -s games.txt
   ```

## 图形界面版数独

可以进入 `Sudoku` 文件夹中，在命令行输入 `python gui.py` 运行图形界面，也可以双击运行 `sudokuGUI.exe` 文件来运行图形界面。

### 界面介绍

数独游戏的界面主要分为4个部分，从上至下依次是：菜单栏、数独棋盘区、数字区、功能区。界面如下图所示：

<img src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/caa61dac-8a85-4152-ab9e-352c7c6ea81d.png" alt="imgbed.cn图床" style="zoom: 67%;" />  

1. 点击 `‘主菜单’` 可以查看 `‘在线帮助’` 和 `‘关于’` 
2. 数独棋盘区用于显示数独题目
3. 数字区用于填写数独
4. 功能区：
   - 删除：删除指定位置的数字
   - 新开局：随机生成一个新的数独开局
   - 自动求解：电脑自动求解当前数独，并将数独终局展示在数独棋盘区
   - 检查：检查当前所填数独是否正确

### 使用演示

1. 点击 `‘新开局’` 生成新的数独开局，界面中灰色的数字是题目已填数字，不可以修改或删除。挖空的数量会在区间 `[30,60]` 之间

   <img src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/82f01cab-6c24-40c3-8211-98f427838da5.gif" alt="imgbed.cn图床" style="zoom: 67%;" />

2. 填写数字，先在数字区选中自己要使用的数字，然后点击要填的空格。

   <img src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/f4f6c6d5-6216-4ee3-8f60-4278750df02f.gif" alt="imgbed.cn图床" style="zoom:67%;" />

3. 删除填错的数字，点击删除键，然后点击要删除的数字。

   <img src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/343c8ab0-0ba0-49fd-ac4c-b32157d0ae0e.gif" alt="imgbed.cn图床" style="zoom: 67%;" />

4. 点击自动求解，电脑会自动求出当前数独的一个终局，并展示在数独棋盘区。

   <img src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/9a49882c-0697-4e6e-b120-2d78c9af640a.gif" alt="imgbed.cn图床" style="zoom:67%;" />

5. 检查。点击检查，系统会提示你当前的数独是否正确完成。

   <img src="https://vkceyugu.cdn.bspapp.com/VKCEYUGU-b1ebbd3c-ca49-405b-957b-effe60782276/398e2dea-f789-40da-936f-45e89ab681d8.gif" alt="imgbed.cn图床" style="zoom:67%;" />
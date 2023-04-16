# 执行文件
"""
井字棋游戏
"""
import sys
from tictactoe_function import print_chess, judge_chess

# 用字典存储井字棋，并用行列组合定位棋子
chess_dict = {'11': ' ', '12': ' ', '13': ' ',
              '21': ' ', '22': ' ', '23': ' ',
              '31': ' ', '32': ' ', '33': ' '}

# 打印初始棋盘，并设定 O 方先手
current_turn = 'O'
print_chess(chess_dict)

# main loop
for i in range(9):
    # 获取玩家落子位置
    while True:
        set_pos = input(f"现在是 {current_turn} 方回合. 输入落子位置\n")
        chess = chess_dict.get(set_pos, False)
        if not chess or chess != ' ':
            print("输入有误")
        else:
            chess_dict[set_pos] = current_turn
            print_chess(chess_dict)
            break
    # 检查是否有人获胜
    if judge_chess(chess_dict):
        print(f"{current_turn} 方获胜\n游戏结束")
        sys.exit()

    # 轮换回合
    if current_turn == 'O':
        current_turn = 'X'
    else:
        current_turn = 'O'

print("平局\n游戏结束")

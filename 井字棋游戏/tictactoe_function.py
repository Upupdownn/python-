# — coding: utf-8 –
# 井字棋游戏函数文件
def print_chess(chess_dict: dict):
    """打印棋盘"""
    print("-------------")
    for i in range(1, 4):
        for j in range(1, 4):
            pos = str(i) + str(j)
            print(f"| {chess_dict[pos]} ", end='')
        print("|")
        print("-------------")


def judge_chess(chess_dict: dict) -> bool:
    """检查棋盘，若有获胜方，返回True，否则False"""
    # 检查中心棋子
    chessman = chess_dict['22']
    if chessman != ' ':
        if (chess_dict['11'] == chessman and chess_dict['33'] == chessman or
                chess_dict['12'] == chessman and chess_dict['32'] == chessman or
                chess_dict['13'] == chessman and chess_dict['31'] == chessman or
                chess_dict['21'] == chessman and chess_dict['23'] == chessman):
            return True

    # 检查左上角棋子
    chessman = chess_dict['11']
    if chessman != ' ':
        if (chess_dict['12'] == chessman and chess_dict['13'] == chessman or
                chess_dict['21'] == chessman and chess_dict['31'] == chessman):
            return True

    # 检查右下角棋子
    chessman = chess_dict['33']
    if chessman != ' ':
        if (chess_dict['13'] == chessman and chess_dict['23'] == chessman or
                chess_dict['31'] == chessman and chess_dict['32'] == chessman):
            return True
    return False

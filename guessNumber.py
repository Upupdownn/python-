"""
随机生成1-100之间的数，不断让玩家猜，直到猜中
提示玩家猜大了还是小了，猜对时给出猜测次数
tips：捕获ValueError，当玩家输入并非数字时，提示玩家并重新输入
"""

import random

# 记录生成的数字和猜的次数
target_num = random.randint(1, 100)
count = 0

# main loop
while True:
    # 得到玩家猜的数字
    while True:
        try:
            player_num = int(input("猜数字，范围在1 - 100：\n"))
        except ValueError as ve:
            print("输入有误，请重新输入")
        else:
            break

    # 计数加1，并判断结果
    count += 1
    if player_num == target_num:
        print(f"猜对了, 你猜了{count}次")
        break
    elif player_num > target_num:
        print("猜大了")
    else:
        print("猜小了")

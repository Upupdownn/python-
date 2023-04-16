"""
输入一个数n，得到前n个斐波拉契数列
分别给出两种方法：1.用循环实现    2.用递归实现
"""

# 全局变量：存储斐波拉契数列（最多100位）
fb_list = [0 for i in range(100)]


def get_fb_in_recur(num: int) -> int:
    """用递归得到斐波拉契数列"""
    global fb_list
    if num < 1:
        return 0
    if num == 1 or num == 2:
        fb_list[num-1] = 1
        return 1
    else:
        result = get_fb_in_recur(num - 2) + get_fb_in_recur(num - 1)
        fb_list[num-1] = result
        return result


def get_fb_in_loop(num: int):
    """用循环得到斐波拉契数列"""
    global fb_list
    if num < 1:
        return
    for i in range(num):
        if i == 0 or i == 1:
            fb_list[i] = 1
        else:
            fb_list[i] = fb_list[i-2] + fb_list[i-1]


# get_fb_in_loop(20)
get_fb_in_recur(20)
print(fb_list)
# 执行文件
"""
模拟通讯录
    从本地“通讯录.txt”文件读入通讯录信息，并对信息进行管理，最后更新到本地文件中
功能包括：
    1.添加联系人(姓名, 电话)
    2.显示联系人
    3.删除联系人
    4.查找联系人
    5.修改联系人
    6.清空联系人
    0.退出通讯录（将内容同步到文件中）
"""

import os
from AddressBook import Person, AddressBook

# 用列表存储联系人信息，列表元素是联系人的类对象
address_list = list()

# 如果同文件目录下有"通讯录.txt"文件，则读入，若没有就创建空列表
try:
    with open("通讯录.txt") as file:
        content = file.readlines()
        del content[0]
except FileNotFoundError as fe:
    pass
else:
    for line in content:
        line = line.split()
        new_person = Person(line[0], line[1])
        address_list.append(new_person)

# 创建通讯录实例
address_book = AddressBook(address_list)

# main loop
while True:
    # 打印主菜单
    address_book.show_menu()

    # 让用户选择功能，以序号表示
    user_select = input("请输入功能序号：\n")
    if user_select == '1':
        # 1.添加联系人
        address_book.add_person()
    elif user_select == '2':
        # 2.显示联系人
        address_book.display_person()
    elif user_select == '3':
        # 3.删除联系人
        address_book.delete_person()
    elif user_select == '4':
        # 4.查找联系人
        address_book.search_person()
    elif user_select == '5':
        # 5.修改联系人
        address_book.modify_person()
    elif user_select == '6':
        # 6.清空联系人
        address_book.clear_person()
    elif user_select == '0':
        # 0.退出通讯录
        address_book.quit_address_book()
    else:
        # 输入有误的情况
        print("输入有误，请重新输入")

    os.system('pause')

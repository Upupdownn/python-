# — coding: utf-8 –
# 类定义文件
import sys

MENU = """**************************
******  1.添加联系人  ******
******  2.显示联系人  ******
******  3.删除联系人  ******
******  4.查找联系人  ******
******  5.修改联系人  ******
******  6.清空联系人  ******
******  0.退出通讯录  ******
**************************"""


# 联系人的类定义
class Person:
    def __init__(self, name: str, tel: str):
        """初始化联系人信息"""
        self.name = name
        self.tel = tel

    def display_info(self):
        """输出姓名和电话"""
        print(f"姓名：{self.name}\t\t电话：{self.tel}")

    def verify_info(self, info: str) -> bool:
        """验证是否是本人，是返回True，不是返回False"""
        if info == self.name or info == self.tel:
            return True
        return False

    def modify_info(self, tel: str):
        """修改电话号码"""
        self.tel = tel


# 通讯录的类定义
class AddressBook:
    def __init__(self, address_list: list):
        """初始化通讯录列表"""
        self.address_list = address_list

    def show_menu(self):
        """显示主菜单"""
        print(MENU)

    def add_person(self):
        """添加联系人"""
        name = input("输入姓名: \n")
        tel = input("输入电话号码：\n")
        new_person = Person(name, tel)
        self.address_list.append(new_person)
        print("添加成功")

    def display_person(self):
        """显示所有联系人信息"""
        if not self.address_list:
            print("通讯录空")
            return
        for person in self.address_list:
            person.display_info()

    def delete_person(self):
        """根据名字删除联系人"""
        name = input("请输入要删除联系人的姓名：\n")
        for person in self.address_list[:]:
            if person.verify_info(name):
                self.address_list.remove(person)
                print("删除成功")
                return
        print("查无此人")

    def search_person(self):
        """根据姓名查找联系人"""
        name = input("请输入要查找联系人的姓名：\n")
        for person in self.address_list:
            if person.verify_info(name):
                person.display_info()
                return
        print("查无此人")

    def modify_person(self):
        """根据姓名修改联系人"""
        name = input("请输入要修改联系人的姓名：\n")
        for person in self.address_list:
            if person.verify_info(name):
                tel = input("请输入电话号码：\n")
                person.modify_info(tel)
                print("修改成功")
                return
        print("查无此人")

    def clear_person(self):
        """清空通讯录"""
        self.address_list = list()
        print("清除成功")

    def quit_address_book(self):
        """保存通讯录至本地文件并退出程序"""
        with open("通讯录.txt", 'w') as file:
            file.write("姓名".ljust(10,) + "电话号码\n")
            for person in self.address_list:
                format_info = f"{person.name.ljust(10)}{person.tel}\n"
                file.write(format_info)
        print("通讯录已更新至本地")
        sys.exit()
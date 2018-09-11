#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2018 - Brian Chen <breeze520@outlook.com>
# version: 1.0
# import: only works in python2
# Last modified: 2018-9-11

""" A simple todo list application """

import os

dbname = "events.db"

# To show all todo list events
# 显示所有待办事项
def todolist():
    # 如果数据库文件不存在，则新建
    if not os.path.exists(dbname):
        os.mknod(dbname)
    else:
        f = open(dbname)
        line = f.readline()
        
        # 如果待办为空
        if line == "":
            print "<空>"

        num = 1  # 待办事项序号
        while line:
            print "[" + str(num) + "]" ,line,
            num += 1
            line = f.readline()

        f.close()

# To show all the options for the menu
# 显示所有操作菜单
def menu():
    print "\n(1) 新增  ",
    print "(2) 完成  ",
    print "(3) 退出"

# Waiting user to input the option
# 输入操作选项
def choose():
    ch = raw_input("请输入你的选择<Enter退出>： ")
    while 1:
        # 选择3 或者无输入，则退出程序
        if ch == "" or ch == "3":
            break
        elif ch == "1":  # 新增
            add()
            break
        elif ch == "2":  # 完成
            complete()
            break
        else:
            ch = raw_input("\n输入错误！请重新输入<Enter退出>： ")

# To add a new todo list event
# 新增操作
def add():
    new_event = raw_input("请输入待办事项<Enter退出>： ")
    # 无输入，则退出到主菜单
    if new_event != "":
        f = open(dbname, "a")
        f.writelines(new_event + "\n")
        f.close()

    main()

# To finish a event
# 完成操作
def complete():
    content = []  # 临时变量，存储所有待办内容
    f = open(dbname)
    line = f.readline()
    while line:
        content.append(line)
        line = f.readline()
    f.close()

    # 判断输入类型
    input_OK = True
    while input_OK:
        try:
            value = raw_input("请输入前面的数字编号<Enter退出>： ")
            # 无输入，则退出到主菜单
            if value == "":
                break

            # 类型转换
            del_num = int(value)

            # 检查输入字数，如果不是一个数字，则重新输入
            input_num = len(value)
            if input_num != 1:
                print "请只输入一个数字！"

            # 如果输入是一个数字    
            else:
                # 输入的数字减去1，对应到Todo索引序号（因为Todo是从0开始计数的）
                num = int(del_num) - 1

                # 检查输入数字的范围
                if num in range(len(content)):
                    del content[num]

                    # 重新写回文件
                    f = open(dbname, "w")
                    for line in content:
                        f.writelines(line)
                    f.close()
                    break

                # 如果超出范围，提示后，要求重新输入
                else:
                    print "输入的数字超出范围！请重新输入。"

        except EOFError, e:
            print e
        except IOError, e:
            print e
        except ValueError, e:
            print e
        else:  # 如果没有异常，则执行
            if type(value) == type(1):
                input_OK = False
        finally: # 不管有没有异常都执行
            print "\n"

    main()

def pic():
    print """
            ╭┐┌╮
            ╭┘└┘└╮
            └┐．．┌┘──╮
            ╭┴──┤★　　├╮
            │ｏ　ｏ│　　　│●
            ╰┬──╯　　　│
            \__|__/_____／
"""

# 主程序main
def main():
    os.system("clear")
    pic()
    print "============= 待办事项 =============\n"
    todolist()
    print "\n===================================="
    menu()
    choose()

# 程序入口
if __name__ == '__main__':
    main()

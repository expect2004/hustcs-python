# coding=utf-8

# 初始化menu1字典，输入两道菜的价格
menu1 = {}
menu1['fish']=int(input())
menu1['pork']=int(input())

# menu_total列表现在只包含menu1字典
menu_total = [menu1]

# 请在此添加代码，实现编程要求
########## Begin ##########

menu2 = {}
for key, val in menu1.items():
    menu2[key] = val * 2
menu_total.append(menu2)
# print(menu_total)

########## End ##########

# 输出menu_total列表
print(menu_total)






# names = ['zhangsan', 'lisi', 'wangwu']
# for name in names:
#     print(f'hello {name},would you like to learn some Python today?')

#   练习3.3:自己的列表 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
#   根据该列表打印一系列有关这些通勤方式的陈述，如下所示。
# names = ['cycle', 'car', 'bus']
# for name in names:
#     print(f'I like {name} to commute.')


# 创建一个摩托车列表，并增加三个品牌的摩托车
# names = ['honda', 'yamaha', 'suzuki']
# print(f'I would like to own a {names}.')
# # 将列表中的第一个元素修改为ducati品牌
# names[0] = 'ducati'
# print(f'I would like to own a {names}.')
# 在列表的末尾添加一个新的品牌摩托车
# names.append('yamaha')
# print(f'I would like to own a {names}.')
# # 先创建一个空的列表，然后使用append()方法将三个新的摩托车添加到列表中
# names = []
# names.append('honda1')
# names.append('yamaha1')
# names.append('suzuki1')
# print(f'I would like to own a {names}.')

# 创建一个列表，并默认创建三个元素，然后在第2个元素位置添加一个新的元素
# names = ['honda', 'yamaha', 'suzuki']
# names.insert(1, 'ducati')
# print(f'I would like to own a {names}.')
# # 删除列表中的第1个元素
# del names[0]
# print(f'I would like to own a {names}.')



# 从motorcycles中弹出一款摩托车
# names = ['honda', 'yamaha', 'suzuki']
# popped_motorcycle = names.pop(0)
# print(f'The popped motorcycle is {popped_motorcycle}.')
# print(f'I would like to own a {names}.')



# 根据值删除元素

# names = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(names)
# names.remove('ducati')
# print(names)

#
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
#
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)

# 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的)，
# 你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印消息，邀请这些人都来与你共进晚餐。
# names = ['zhangsan', 'lisi', 'wangwu']
# for name in names:
#     print(f'hello {name},would you like to join me for dinner?')
#
# print(f'but  {names[2]} not come.')
#
# names[2] = 'aaaaaaa'
# print(f'hello {names[2]},would you like to join me for dinner?')
# print(names)

# 使用三国演义中的五个常用人物，创建一个列表，并打印一条消息，指出他们正在参加一个游戏。
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# 按姓氏拼音进行排序
names.sort()
print(f'{names} are playing a game.')
# name="Zhao Wenming"
# print(f'hello {name},would you like to learn some Python today?')
# name="Zhao Wenming"
# # 分别按名字全小写、全大写、首字母大写输出三条
# print(f'hello {name.lower()},would you like to learn some Python today?')
# print(f'hello {name.upper()},would you like to learn some Python today?')
# print(f'hello {name.title()},would you like to learn some Python today?')

# message = '宫崎骏:愿你遍历山河，觉得"人间"值得'
# print(message)
# famous_name="宫崎骏"
# message = f'{famous_name}:愿你遍历山河，觉得"人间"值得'
# print(message)

#练习2.7:删除人名中的空白 用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。
#务必至少使用字符组合"t"和"n"各一次。
# name=" Zhao Wenming "
# print(f'hello {name.lstrip()},\twould you like to learn some Python today?')
# print(f'hello {name.rstrip()},\nwould you like to learn some Python today?')
# print(f'hello {name.strip()},would you like to learn some Python today?')
filename='pi_digits.txt'
print( filename.removeprefix('pi_digits'))
print( filename.removesuffix('.txt'))
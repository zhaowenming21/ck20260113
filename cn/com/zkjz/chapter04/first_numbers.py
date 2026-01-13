# for value in range(2,15):
#     print(value)

# numbers = list(range(2, 15,2))
# print(numbers)

# ns= range(1,11)
# numbers = list(range(1, 11))
# print( ns)
# print( numbers)
# squares = []
# for value in ns:
#     square = value ** 2
#     squares.append(square)
# print(squares)

# 定义一个含有10个数字的列表
# numbers = list(range(10))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(sum(numbers) / len(numbers))

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# for value in range(0,21):
#     print(value)
# 提供一个切片的例子
# numbers = list(range(0, 21, 1))
# print(numbers[0:3])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[8:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# 遍历切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
#
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

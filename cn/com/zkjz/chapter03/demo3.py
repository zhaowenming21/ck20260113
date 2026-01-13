# 创建包含三国演义五位人物的列表
names = ['关羽', '张飞', '赵云', '马超', '黄忠']

# 按姓氏拼音进行排序（注：Python默认的sort对中文拼音排序不准确，这里用pypinyin库实现精准排序）
# 先安装依赖：pip install pypinyin
from pypinyin import lazy_pinyin

# 按姓氏的拼音首字母排序
names_sorted = sorted(names, key=lambda x: lazy_pinyin(x)[0])

# 格式化输出自然的中文消息
# 将列表转为"XX、XX、XX、XX和XX"的格式
if len(names_sorted) > 1:
    print(','.join(names_sorted[:-1]))
    print(names_sorted[-1])
    name_str = '、'.join(names_sorted[:-1]) + '和' + names_sorted[-1]
else:
    name_str = names_sorted[0]

# 打印消息
print(f'{name_str} 正在参加一个游戏。')
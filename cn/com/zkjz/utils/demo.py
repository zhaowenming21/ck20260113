"""
工具类使用示例
"""

from cn.com.zkjz.utils import StringUtils, ListUtils, MathUtils, FileUtils


def string_utils_demo():
    """字符串工具类示例"""
    print("=== 字符串工具类示例 ===")
    text = "Hello World"
    print(f"原字符串: {text}")
    print(f"反转: {StringUtils.reverse(text)}")
    print(f"单词首字母大写: {StringUtils.capitalize_words(text)}")
    print(f"元音字母数量: {StringUtils.count_vowels(text)}")
    
    palindrome = "A man a plan a canal Panama"
    print(f"'{palindrome}' 是回文吗? {StringUtils.is_palindrome(palindrome)}")
    print()


def list_utils_demo():
    """列表工具类示例"""
    print("=== 列表工具类示例 ===")
    nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
    print(f"嵌套列表: {nested_list}")
    print(f"展平后: {ListUtils.flatten(nested_list)}")
    
    duplicate_list = [1, 2, 3, 2, 4, 1, 5]
    print(f"原列表: {duplicate_list}")
    print(f"去重后: {ListUtils.remove_duplicates(duplicate_list)}")
    
    chunked = ListUtils.flatten(nested_list)
    print(f"分块(大小3): {ListUtils.chunk(chunked, 3)}")
    
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7]
    print(f"列表1: {list1}")
    print(f"列表2: {list2}")
    print(f"交集: {ListUtils.intersection(list1, list2)}")
    print(f"差集: {ListUtils.difference(list1, list2)}")
    print()


def math_utils_demo():
    """数学工具类示例"""
    print("=== 数学工具类示例 ===")
    print(f"5的阶乘: {MathUtils.factorial(5)}")
    print(f"12和18的最大公约数: {MathUtils.gcd(12, 18)}")
    print(f"12和18的最小公倍数: {MathUtils.lcm(12, 18)}")
    print(f"17是质数吗? {MathUtils.is_prime(17)}")
    print(f"前10个斐波那契数: {MathUtils.fibonacci(10)}")
    print(f"[1, 2, 3, 4, 5]的平均值: {MathUtils.average([1, 2, 3, 4, 5])}")
    print()


def file_utils_demo():
    """文件工具类示例"""
    print("=== 文件工具类示例 ===")
    
    # 创建一个临时目录
    temp_dir = "temp"
    FileUtils.ensure_dir_exists(temp_dir)
    print(f"确保目录 '{temp_dir}' 存在")
    
    # 写入文本文件
    text_file = f"{temp_dir}/example.txt"
    FileUtils.write_text(text_file, "这是一个示例文本文件")
    print(f"写入文本文件: {text_file}")
    
    # 读取文本文件
    content = FileUtils.read_text(text_file)
    print(f"读取内容: {content}")
    
    # 写入JSON文件
    json_file = f"{temp_dir}/data.json"
    data = {"name": "张三", "age": 30, "hobbies": ["读书", "游泳", "编程"]}
    FileUtils.write_json(json_file, data)
    print(f"写入JSON文件: {json_file}")
    
    # 读取JSON文件
    json_data = FileUtils.read_json(json_file)
    print(f"读取JSON数据: {json_data}")
    
    # 获取文件大小
    size = FileUtils.get_file_size(text_file)
    print(f"文件大小: {size} 字节")
    
    # 检查文件是否存在
    exists = FileUtils.file_exists(text_file)
    print(f"文件存在: {exists}")
    print()


if __name__ == "__main__":
    string_utils_demo()
    list_utils_demo()
    math_utils_demo()
    file_utils_demo()
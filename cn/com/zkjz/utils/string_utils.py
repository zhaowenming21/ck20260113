"""
字符串工具类
提供字符串处理相关的常用方法
"""


class StringUtils:
    """字符串处理工具类"""
    
    @staticmethod
    def is_empty(s):
        """判断字符串是否为空或只包含空白字符"""
        return not s or s.strip() == ""
    
    @staticmethod
    def reverse(s):
        """反转字符串"""
        return s[::-1]
    
    @staticmethod
    def capitalize_words(s):
        """将每个单词首字母大写"""
        return ' '.join(word.capitalize() for word in s.split())
    
    @staticmethod
    def is_palindrome(s):
        """判断字符串是否为回文"""
        # 忽略大小写和空格
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def count_vowels(s):
        """统计字符串中元音字母的数量"""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)
    
    @staticmethod
    def remove_duplicates(s):
        """移除字符串中的重复字符，保留第一次出现的字符"""
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
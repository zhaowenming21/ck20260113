"""
文件工具类
提供文件操作相关的常用方法
"""
import os
import json
import pickle


class FileUtils:
    """文件操作工具类"""
    
    @staticmethod
    def read_text(file_path, encoding='utf-8'):
        """读取文本文件"""
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    
    @staticmethod
    def write_text(file_path, content, encoding='utf-8'):
        """写入文本文件"""
        with open(file_path, 'w', encoding=encoding) as file:
            file.write(content)
    
    @staticmethod
    def read_json(file_path, encoding='utf-8'):
        """读取JSON文件"""
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)
    
    @staticmethod
    def write_json(file_path, data, indent=4, encoding='utf-8'):
        """写入JSON文件"""
        with open(file_path, 'w', encoding=encoding) as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def read_pickle(file_path):
        """读取pickle文件"""
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    
    @staticmethod
    def write_pickle(file_path, data):
        """写入pickle文件"""
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
    
    @staticmethod
    def ensure_dir_exists(dir_path):
        """确保目录存在，不存在则创建"""
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
    @staticmethod
    def get_file_size(file_path):
        """获取文件大小（字节）"""
        return os.path.getsize(file_path)
    
    @staticmethod
    def file_exists(file_path):
        """检查文件是否存在"""
        return os.path.exists(file_path)
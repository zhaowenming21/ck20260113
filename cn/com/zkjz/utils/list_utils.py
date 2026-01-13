"""
列表工具类
提供列表处理相关的常用方法
"""


class ListUtils:
    """列表处理工具类"""
    
    @staticmethod
    def flatten(lst):
        """将嵌套列表展平为一维列表"""
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(ListUtils.flatten(item))
            else:
                result.append(item)
        return result
    
    @staticmethod
    def remove_duplicates(lst):
        """移除列表中的重复元素，保留原始顺序"""
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    @staticmethod
    def chunk(lst, size):
        """将列表分割成指定大小的块"""
        return [lst[i:i + size] for i in range(0, len(lst), size)]
    
    @staticmethod
    def is_sorted(lst, reverse=False):
        """检查列表是否已排序"""
        if reverse:
            return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
        else:
            return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    @staticmethod
    def intersection(lst1, lst2):
        """返回两个列表的交集"""
        return list(set(lst1) & set(lst2))
    
    @staticmethod
    def difference(lst1, lst2):
        """返回在lst1中但不在lst2中的元素"""
        return list(set(lst1) - set(lst2))
"""
数学工具类
提供数学计算相关的常用方法
"""


class MathUtils:
    """数学计算工具类"""
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n < 0:
            raise ValueError("阶乘只能计算非负整数")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def gcd(a, b):
        """计算最大公约数（欧几里得算法）"""
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a, b):
        """计算最小公倍数"""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // MathUtils.gcd(a, b)
    
    @staticmethod
    def is_prime(n):
        """判断是否为质数"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def fibonacci(n):
        """生成斐波那契数列的前n项"""
        if n <= 0:
            return []
        if n == 1:
            return [0]
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib
    
    @staticmethod
    def average(numbers):
        """计算平均值"""
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
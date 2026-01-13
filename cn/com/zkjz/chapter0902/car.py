"""一组用于表示燃油汽车和电动汽车的类"""


class Car:
    """一次模拟汽车的简单尝试
        """

    def __init__(self, make, model, year):
        """初始化汽车的属性
        参数：
            make (str): 汽车的品牌。
            model (str): 汽车的型号。
            year (int): 汽车的生产年份。
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回一个 neatly-formatted descriptive name."""
        long_name = f"车辆的信息如下：{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车的里程数"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"Odometer reading updated to {self.odometer_reading} miles.")
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        print(f"Odometer reading incremented by {miles} miles.")

    def fill_gas_tank(self):
        """打印一条消息，指出汽车有多少升的油"""
        print(f"这辆车有 {self.gas_tank_size} 升的油箱.")

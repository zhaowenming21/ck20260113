from cn.com.zkjz.chapter0902.car import Car
from cn.com.zkjz.chapter0902.electric_car import ElectricCar

if __name__ == '__main__':
    my_car = Car('audi', 'a4', 2024)
    print(my_car.get_descriptive_name())

    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())

class Yichang:
    def __init__(self, yichang):
        self.yichang = yichang
    def a(self):
        print(5/10)




if __name__ == '__main__':
    yichang = Yichang(10)
    try:
        yichang.a()
    except ZeroDivisionError:
        print("除数不能为0")



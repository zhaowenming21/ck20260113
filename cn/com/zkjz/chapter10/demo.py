import json
from pathlib import Path


class Demo:

    def demo1(self):
        username = input("请输入用户名: ")
        path = Path("username.json")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"再次访问时，用户名是: {username}")


if __name__ == '__main__':
    demo = Demo()
    demo.demo1()

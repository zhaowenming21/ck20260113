import json
from pathlib import Path


class Demo3:

    @staticmethod
    def demo3():
        path = Path("username.json")
        if path.exists():
            contents = path.read_text()
            username = json.loads(contents)
            print(f"欢迎回来，{username}！")
        else:
            username = input("请输入用户名: ")
            path.write_text(json.dumps(username))
            print(f"再次访问时，用户名是: {username}")


if __name__ == '__main__':
    demo3 = Demo3()
    demo3.demo3()

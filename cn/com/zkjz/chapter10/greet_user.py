import json
from pathlib import Path


class Demo2:

    def demo2(self):
        path = Path("username.json")
        contents = path.read_text()
        self.username = json.loads(contents)
        print(f"欢迎回来，{self.username}！")


if __name__ == '__main__':
    demo2 = Demo2()
    demo2.demo2()

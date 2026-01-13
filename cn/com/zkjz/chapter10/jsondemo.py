import json
from pathlib import Path


class JsonDemo:
    def __init__(self, json_str):
        self.json_str = json_str


    def demo1(self):
        numbers = [2, 3, 5, 7, 11, 13]
        path = Path('numbers.json')
        contents = json.dumps(numbers)
        path.write_text(contents)


    def demo2(self):

        path = Path('numbers.json')
        contents = path.read_text()
        numbers = json.loads(contents)

        print(numbers)

if __name__ == '__main__':
    json_demo = JsonDemo('{"numbers": [2, 3, 5, 7, 11, 13]}')
    json_demo.demo2()

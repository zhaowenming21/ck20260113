from pathlib import Path


class WriteMessage:
    def write_message(self, message, filename='message.txt', encoding='utf-8'):
        """
        将消息写入文件，支持指定编码

        参数:
            message (str): 要写入的消息
            filename (str): 要写入的文件名，默认为message.txt
            encoding (str): 文件编码，默认为utf-8
        """
        try:
            path = Path(filename)
            path.write_text(message, encoding=encoding)
            print(f"消息已成功写入文件 {filename}")
        except Exception as e:
            print(f"写入文件时发生错误: {e}")

if __name__ == '__main__':
    writemessage = WriteMessage()
    writemessage.write_message("这是一条测试消息\nssssssssssssss\ndddddddd")

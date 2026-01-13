from pathlib import Path

class FileReader:


    def read_file_content(self, filename, encoding='utf-8'):
        """
        读取文件内容，支持指定编码

        参数:
            filename (str): 要读取的文件名
            encoding (str): 文件编码，默认为utf-8

        返回:
            str: 文件内容，如果文件不存在则返回None
        """
        try:
            path = Path(filename)
            return path.read_text(encoding=encoding).rstrip()
        except FileNotFoundError:
            print(f"文件 {filename} 不存在。")
            return None
        except UnicodeDecodeError:
            print(f"无法解码文件 {filename}，请检查文件编码。")
            return None
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
            return None

    def process_pi_digits(self, content):
        """
        处理π数字内容

        参数:
            content (str): 文件内容

        返回:
            str: 处理后的内容
        """
        if content:
            # 移除所有空白字符，只保留数字和小数点
            return ''.join(c for c in content if c.isdigit() or c == '.')
        return None

if __name__ == '__main__':
    filename = 'text_files/pi_digits.txt'
    filereader = FileReader()
    content = filereader.read_file_content(filename)
    
    if content is not None:
        # print("原始文件内容:")
        # print(content)
        
        # processed = filereader.process_pi_digits(content)
        # print("\n处理后的π数字:")
        # print(processed)
        lines = content.splitlines()
        pi_string = ''
        i = 1
        for line in lines:
            print(f"第{i}行: {line}")
            pi_string += line
            i += 1
        print(pi_string)
        print(len(pi_string))

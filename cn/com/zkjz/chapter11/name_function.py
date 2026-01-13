class NameFunction:
    def get_formatted_name(self, first, last):
        full_name = f"{first} {last}"
        return full_name.title()


if __name__ == '__main__':
    namefunction = NameFunction()
    print(namefunction.get_formatted_name('james', 'bond'))

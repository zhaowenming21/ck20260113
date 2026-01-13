from cn.com.zkjz.chapter11.name_function import NameFunction

if __name__ == '__main__':
    print("Enter 'q' at any time to quit.")
    while True:
        first = input("\nPlease give me a first name: ")
        if first == 'q':
            break
        last = input("Please give me a last name: ")
        if last == 'q':
            break

        formatted_name = NameFunction().get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")
        print('111111111')
        print(222222)
from cn.com.zkjz.chapter11.name_function import NameFunction


class TestNameFunction:
    def test_get_formatted_name(self):
        name_function = NameFunction()
        formatted_name = name_function.get_formatted_name('james',  'bond')
        assert formatted_name == 'James Bond'

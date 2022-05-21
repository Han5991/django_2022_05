import unittest


class UtilsTestCase(unittest.TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    def test_failing(self):
        self.assertEqual('incorrect', to_str('hello'))


def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError(f'str이나 bytes를 전달해야합니다.')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
# driver = webdriver.Chrome('./chromedriver')
# driver.close()

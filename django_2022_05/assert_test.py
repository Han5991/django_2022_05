import unittest


def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y


def fn_add(x, y):
    return x + y


class PartialTest(unittest.TestCase):
    def test_add(self):
        ret = fn_add(10, 10)
        self.assertEqual(ret, 25)

    def test_str(self):
        ret = fn_add('python', 'test')
        self.assertEqual(ret, 'python-hello')


## 익셉션 -> Exception(마더) 메모리의 구조가 OOP로 잘 되어있는건가
if __name__ == '__main__':
    add(10, 20)
    add('10', '20')

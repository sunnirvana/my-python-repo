import unittest
from MyDict import MyDict


class TestMyDict(unittest.TestCase):
    # setUp 和 tearDown 会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('Set up...')

    def tearDown(self):
        print('Tear down...')

    def test_init(self):
        d = MyDict(a=1, b='c')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'c')
        self.assertIsInstance(d, MyDict)

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_keyerror_failed(self):
        d = MyDict(**{'empty': 'empty'})
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty


# Or run unit test with "python -m unittest mydict_test"
if __name__ == '__main__':
    unittest.main()

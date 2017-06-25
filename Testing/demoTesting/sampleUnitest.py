import unittest


def fun(x):
    return x + 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(fun(5),6)
import unittest


class Test_math(unittest.TestCase):

    def setUp(self):
        self.a = 5
        self.b = 0
        self.c = 2

    def test_sub(self):
        sub = self.a / self.b
        return sub

    def test_add(self):
        adt = self.a + self.c
        return adt

    def tearDown(self):
        pass

from random import randint
from unittest import TestCase
class GameNumber(TestCase):
    def __init__(self,a):
        super().__init__()
        self.a = a
        self.b = input('Please input number range 1-6:')
    def test_isdigit(self):
        return self.b.isdigit()
    def test_range(self):
        try:
            self.assertIn(int(self.b),list(range(1,7)))
        except AssertionError as e:
            print(e)
            return False
        else:
            return True
    def test_equal(self):
        try:
            self.assertEqual(self.a, int(self.b))
        except AssertionError as f:
            print (f)
            return False
        else:
            return True
    def test_quiet(self):
        if self.b == 'q':
            print('Give Up !')
            print('You Lost !')
            return False
        return True
    def game_over(self):
        print('Congratulations !  You Guess')
        print('Game Over !')


if __name__ == '__main__':
    active = True
    while active:
        a =randint(1,6)
        print(' new number is %d'%(a))
        cnumber = GameNumber(a)
        if not cnumber.test_quiet():
            break
        if not cnumber.test_isdigit():
            continue
        if not cnumber.test_range():
            continue
        if not cnumber.test_equal():
            continue
        cnumber.game_over()
        active = False

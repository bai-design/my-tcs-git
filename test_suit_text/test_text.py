from test_suit_text import test_math
import unittest

if __name__ == '__main__':
    # 创建测试套件
    text_test = unittest.TestSuite()
    # 将测试方法“test_sub”加入测试套件
    text_test.addTest(test_math.Test_math("test_sub"))
    # 需测试方法“test_add”加入测试套件
    text_test.addTest(test_math.Test_math("test_add"))
    # 创建TextTestRunner实列
    text_run = unittest.TextTestRunner()
    # 通过TextTestRunner实列运行测试套件内测试方法
    text_run.run(text_test)

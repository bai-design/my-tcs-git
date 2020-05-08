import HTMLTestRunner
import time
import unittest

if __name__ == '__main__':
    # 创建测试套件
    text_test = unittest.TestSuite()
    # 在当前目录寻找所有test*.py文件
    discover = unittest.defaultTestLoader.discover(start_dir='./', pattern='test*.py')
    # 将所得文件加入测试套件（规范：模块内方法均以“test”开头）
    text_test.addTest(discover)
    # 格式化当前时间
    file_time = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
    # html文件路径
    file_name = '/usr/local/sln-pro/my-tcs-git/tcs/report/%s.html' % file_time
    # 以二进制写方式打开html文件
    file = open(file_name, 'wb')
    # 创建HTMLTestRunner实列
    html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='Test', description='First')
    # 通过HTMLTestRunner实例运行测试套件内测试方法
    html_runner.run(text_test)
    # 关闭html文件
    file.close()

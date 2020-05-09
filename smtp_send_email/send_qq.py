from smtp_send_email.send_email import Send_email
import os

if __name__ == '__main__':
    """
        1.以下代码不能被其他模块调用
        2.实现自动化发送最新测试报告
    """
    # 报告目录
    result_dir = '/usr/local/sln-pro/my-tcs-git/tcs/report'
    # 获取报告目录下所有文件及目录名册
    lists = os.listdir(result_dir)
    # lambda自定义函数：类型为文件，返回创建时间；否则，返回 0 。根据返回值对列表进行永久排序：从小到大
    lists.sort(
        key=lambda fn: os.path.getmtime(result_dir + "/" + fn) if not os.path.isdir(result_dir + "/" + fn) else 0)
    # 获取列表内倒数第一的文件目录
    path = result_dir + '/' + lists[-1]
    # 获取列表内倒数第一的文件名称
    file_rename = lists[-1]
    # 邮件接收者
    receiver = '1710448461@qq.com'
    # 创建Send_email实列
    sends = Send_email(receiver)
    # 调用msg方法，返回需发送的邮件内容
    msgs = sends.msg(path, file_rename)
    # 调用send_email发送，发送邮件
    sends.send_email(msgs)

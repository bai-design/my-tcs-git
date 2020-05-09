import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_email(object):

    """实现发送邮件功能"""

    def __init__(self, recever):
        """
            构造函数，初始化以下参数：

            self.recever：邮件接收者
            self.sever ：邮箱服务器
            self.sender ：邮件发送者
            self.username ：邮箱用户
            self.password ：邮箱授权码

        """
        self.recever = recever
        self.sever = 'smtp.qq.com'
        self.sender = '1659935784@qq.com'
        self.username = '1659935784@qq.com'
        self.password = 'yknmfsvzoqsgdbcc'

    def msg(self, path, file_names):

        """构造邮件内容"""

        # 创建MIMEMultipart（）实列，mixed参数 值：邮件内可以存在附件、正文、图片等元素
        msg = MIMEMultipart('mixed')
        # 邮件标题
        subject = 'python_test'
        msg['Subject'] = subject
        # 邮件发送者
        msg['From'] = self.sender
        # 邮件接收者
        msg['To'] = self.recever
        # 待发送文件路径
        filename = path
        # 二进制读模式打开文件
        file = open(filename, 'rb')
        # 读取文件内容
        file_object = file.read()
        # 开始构造附件
        # 创建 MIMEText（）实列  html 参数：文件类型  utf-8 文本格式
        att = MIMEText(file_object, 'html', 'utf-8')
        # 以流的形式上传文件
        att['Content-Type'] = 'application/octet-stream'
        # 标注上传的文件为邮件的附件，命名附件名称
        att.add_header('Content-Disposition', 'attachment', filename='{}'.format(file_names))
        # 附件构造完成
        msg.attach(att)
        # 关闭文件
        file.close()
        # 返回邮件内容
        return msg

    def send_email(self, msg):
        """发送邮件"""
        # 创建SMTP()实列
        smtp = smtplib.SMTP()
        # 链接smtp服务器
        smtp.connect(self.sever)
        # 登录服务器
        smtp.login(self.username, self.password)
        # 发送邮件 sender:邮件发送者 recever: 邮件接收者 msg.as_string(): 邮件内容
        smtp.sendmail(self.sender, self.recever, msg.as_string())
        # 登出服务器
        smtp.quit()



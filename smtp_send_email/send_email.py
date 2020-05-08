import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_email(object):

    def __init__(self, recever):
        self.recever = recever
        self.sever = 'smtp.qq.com'
        self.sender = '1659935784@qq.com'
        self.username = '1659935784@qq.com'
        self.password = 'yknmfsvzoqsgdbcc'

    def msg(self, path, file_names):
        msg = MIMEMultipart('mixed')
        subject = 'python_test'
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = self.recever
        filename = path
        file = open(filename, 'rb')
        file_object = file.read()
        att = MIMEText(file_object, 'html', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename='{}'.format(file_names))
        msg.attach(att)
        file.close()
        return msg

    def send_email(self, msg):
        smtp = smtplib.SMTP()
        smtp.connect(self.sever)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.username, self.recever, msg.as_string())
        smtp.quit()



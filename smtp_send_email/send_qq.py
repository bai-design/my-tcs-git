from smtp_send_email.send_email import Send_email
import os
if __name__ == '__main__':
    result_dir = '/usr/local/sln-pro/my-tcs-git/tcs/report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "/" + fn) if not os.path.isdir(result_dir + "/" + fn) else 0)
    path = result_dir + '/' + lists[-1]
    file_rename = lists[-1]
    receiver = '1710448461@qq.com'
    sends = Send_email(receiver)
    msgs = sends.msg(path, file_rename)
    sends.send_email(msgs)

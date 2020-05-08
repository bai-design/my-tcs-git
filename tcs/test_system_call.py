import os
import shutil
def system_call(lists_gits):
    for lists_git in lists_gits:
        os.system("git clone git@github.com:bai-design/%s.git"%(lists_git))

if __name__ == '__main__':
    lists_gits = ['my-world-git']
    print(os.getcwd())
    os.chdir('/usr/local/sln-pro')
#    file = os.popen('ls')
 #   file_readers = file.readlines()
#    print(file_readers)
    print(os.getcwd())
 #   print(os.listdir('/usr/local/sln-pro'))
    if 'my-world-git' in os.listdir('/usr/local/sln-pro'):
        shutil.rmtree('my-world-git')
        system_call(lists_gits)
    else:
        system_call(lists_gits)

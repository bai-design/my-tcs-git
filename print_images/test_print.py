import os
import sys
from read_write_apend_xls.read_xls import Read_excle_xls
from print_images.print_image import Print_Image
sys.path.append('/usr/local/sln-pro/my-tcs-git/print_image')
if __name__ == '__main__':
    # 文件路径
    if 'image' not in os.listdir('/usr/local/sln-pro/my-tcs-git/tcs/'):
        os.system('mkdir /usr/local/sln-pro/my-tcs-git/tcs/image')
    book_name_xls = '/usr/local/sln-pro/my-tcs-git/tcs/work_xls/电话簿.xls'
    image_path = '/usr/local/sln-pro/my-tcs-git/tcs/image/'
    #sheet页名称
    sheet_name_xls_00 = 'dkd-alphone'
    #创建读取实列
    read_book = Read_excle_xls(book_name_xls,sheet_name_xls_00)
    # 调用read_excle_rows_xls（）返回 返回字典 key值为行数 value值为行内容
    image_lists = read_book.read_excle_rows_xls()
    # 获取每行每列值
    for i in range(1, len(image_lists)):
        # 部门（职位）
        im_org = image_lists[str(i)][0]
        # 姓名
        im_name = image_lists[str(i)][1]
        # 电话
        im_telephone = image_lists[str(i)][3]
        # 邮箱
        im_email = image_lists[str(i)][4]
        # 创建 Print_Image（）实列
        one_person = Print_Image(im_org, im_name, im_telephone, im_email)
        # 调用get_vard（）方式生成个人信息二维码图片
        one_person.get_vard(image_path)





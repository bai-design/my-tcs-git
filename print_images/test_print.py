import os
import sys
from read_write_apend_xls.read_xls import Read_excle_xls
from print_image.print_image import Print_Image
sys.path.append('/usr/local/sln-pro/my-tcs-git/print_image')
if __name__ == '__main__':
    # 文件路径
    if 'image' not in os.listdir('/usr/local/sln-pro/my-tcs-git/tcs'):
        os.system('mkdir /usr/local/sln-pro/my-tcs-git/tcs/image')
    book_name_xls = '/usr/local/sln-pro/my-tcs-git/tcs/work_xls/电话簿.xls'
    image_path = '/usr/local/sln-pro/my-tcs-git/tcs/image/'
    #sheet页名称
    sheet_name_xls_00 = 'dkd-alphone'
    read_book = Read_excle_xls(book_name_xls,sheet_name_xls_00)
    image_lists = read_book.read_excle_rows_xls()
    for i in range(0, len(image_lists)):
        im_org = image_lists[i][0]
        im_name = image_lists[i][1]
        im_voice = image_lists[i][2]
        im_telephone = image_lists[i][3]
        im_email = image_lists[i][4]
        one_person = Print_Image(im_org, im_name, im_voice, im_telephone, im_email)
        one_person.get_vard(image_path)





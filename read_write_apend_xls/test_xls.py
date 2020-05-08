import os
from read_write_apend_xls.create_xls import Create_excel_xls
from read_write_apend_xls.write_xls import Write_excel_xls_append
from read_write_apend_xls.read_xls import Read_excle_xls

if __name__ == '__main__':
    # 文件路径
    if 'work_xls' not in os.listdir('/usr/local/sln-pro/my-tcs-git/tcs'):
        os.system('mkdir /usr/local/sln-pro/my-tcs-git/tcs/work_xls')
    book_name_xls = '/usr/local/sln-pro/my-tcs-git/tcs/work_xls/电话簿.xls'
    #sheet页名称
    sheet_name_xls_00 = 'dkd-alphone'
    sheet_name_xls_01 = 'kangheng-alphone'
    sheet_name_xls_02 = 'family-alphone'
    vaule_append_01 = [["部门（职位）", "姓名", "分机号", "手机号","邮箱"],
                       ["总经理", "魏秀梅", "800", "13323399527", "lucywei@canic.com.cn"],
                       ["人力资源部", "塔娜", "801", "13920390361", "tana@canic.com.cn"]]
    vaule_append_02 = [["财务部", "周志坚", "802", "13920497297", "zhouzj@canic.com.cn"],
                       ["财务部", "李惠言", "803", "13602071056", "lihy@canic.com.cn"]]

#    creat_book = Create_excel_xls(book_name_xls, sheet_name_xls_00, sheet_name_xls_01, sheet_name_xls_02)
#    creat_book.create_excel_xls()
#    write_book = Write_excel_xls_append(book_name_xls, vaule_append_01, sheet_name_xls_00)
#    write_book.write_excel_xls_append()
#    write_book_01 = Write_excel_xls_append(book_name_xls, vaule_append_02, sheet_name_xls_00)
#    write_book_01.write_excel_xls_append()
    read_book = Read_excle_xls(book_name_xls,sheet_name_xls_00)
    read_book.read_excle_xls()






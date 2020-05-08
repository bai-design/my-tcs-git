import os
from read_write_apend_xlsx.read_xlsx import Read_excle_xlsx
from read_write_apend_xlsx.create_xlsx import Create_excel_xlsx
from read_write_apend_xlsx.write_xlsx import Write_excel_xlsx_append

if __name__ == '__main__':
    # 文件路径
    if 'work_xlsx' not in os.listdir('/usr/local/sln-pro/my-tcs-git/tcs'):
        os.system('mkdir /usr/local/sln-pro/my-tcs-git/tcs/work_xlsx')
    book_name_xlsx = '/usr/local/sln-pro/my-tcs-git/tcs/work_xlsx/电话簿.xlsx'
    #sheet页名称
    sheet_name_xlsx_00 = 'dkd-alphone'
    sheet_name_xlsx_01 = 'kangheng-alphone'
    sheet_name_xlsx_02 = 'family-alphone'
    vaule_append_01 = [["部门（职位）", "姓名", "分机号", "手机号","邮箱"],
                       ["总经理", "魏秀梅", "800", "13323399527", "lucywei@canic.com.cn"],
                       ["人力资源部", "塔娜", "801", "13920390361", "tana@canic.com.cn"]]
    vaule_append_02 = [["财务部", "周志坚", "802", "13920497297", "zhouzj@canic.com.cn"],
                       ["财务部", "李惠言", "803", "13602071056", "lihy@canic.com.cn"]]

    creat_book = Create_excel_xlsx(book_name_xlsx, sheet_name_xlsx_00, sheet_name_xlsx_01, sheet_name_xlsx_02)
    creat_book.create_excel_xlsx()
    write_book = Write_excel_xlsx_append(book_name_xlsx,vaule_append_01,sheet_name_xlsx_00)
    write_book.write_excel_xlsx_append()
    read_book = Read_excle_xlsx(book_name_xlsx, sheet_name_xlsx_00)
    read_book.read_excle_xlsx()





import xlwt
import os
import xlrd
from xlutils.copy import copy
#def write_excel_xls(path,sheet_num,value,*sheet_names):

def create_excel_xls(path,*sheet_names):
    """创建xls文件与sheet页"""
    index = len(value)
    workbook = xlwt.Workbook()
    for sheet_name in sheet_names:
        workbook.add_sheet(sheet_name)
#    sheet = workbook.get_sheet(sheet_num)
#    sheet = workbook.get_sheet(workbook.sheet_index(sheet_name))
#    if value:
#        for i in range(0, index):
#            for j in range(0, len(value[i])):
#               sheet.write(i, j, value[i][j])
#    else:
#        print('第一次未写入任何内容')
    workbook.save(path)
    print('OK')
#按sheet页名称读取内容
def read_excle_xls(path,sheet_name):
#按sheet页页码读取内容
#def read_excle_xls(path, sheet_name):
    """读取xls文件某sheet页内容"""
    work_book = xlrd.open_workbook(path)
    sheets = work_book.sheet_names()
    print(sheets)
    print('打印sheet页名称')
    for index,value in enumerate(sheets):
       print('第%s页名称: %s'%(index+1,value))
    #sheet页页码
#    worksheet = work_book.sheet_by_index(sheet_num)
    #sheet页名称
    worksheet  = work_book.sheet_by_name(sheet_name)
    #读取sheet页内容
    #判断sheet页内容是否为空
    if worksheet.nrows:
        print('读取%s页内容'%sheet_name)
        read(worksheet)
    else:
        print('%s页内容为空' % sheet_name)

def read(worksheet):
    """读取sheet页内容"""
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            # 逐行逐列读取数据
            print(worksheet.cell_value(i, j), "\t", end='')
        print()

def write_excel_xlx_append(path,vaule,sheet_name):

    """向xls文件内写入（追加）内容"""

    #写入内容格式[[], [],[]..]
    #写入内容行数
    index = len(vaule)
    #读模式打开文件
    work_book = xlrd.open_workbook(path)
    #定位sheet页
    work_sheet = work_book.sheet_by_name(sheet_name)
    #sheet页数据行数
    rows_old = work_sheet.nrows
    print('原sheet页数据行数为%s'%(rows_old-1))
    #将读模式转换为写模式
    new_work_book = copy(work_book)
    #重新定位sheet页
    sheet_num =new_work_book.sheet_index(sheet_name)
    new_work_sheet = new_work_book.get_sheet(sheet_num)
    #追加内容
    for i in range(0, index):
        for j in range(0, len(vaule[i])):
            new_work_sheet.write(rows_old+i, j, vaule[i][j])
    print('写入完成，%s页数据行数为: %s'%(sheet_name, rows_old+index-1))
    #保存文件
    new_work_book.save(path)
    print('新数据保存成功')












if __name__ == '__main__':

    if 'work_book' not in os.listdir('/usr/local/sln-pro/my-tcs-git/tcs'):
        """检查保存文件目录是否存在，若不存在则创建"""
        os.mkdir('work_book')

    # 文件路径
    book_name_xls = '/usr/local/sln-pro/my-tcs-git/tcs/work_book/电话簿.xls'
    #sheet页名称
    sheet_name_xls_00,sheet_name_xls_01,sheet_name_xls_02 ='dkd-alphone','kangheng-alphone','family-alphone'

#    value_title =''
#    value_title = [["部门（职位）", "姓名", "分机号", "手机号","邮箱"],
#    ["总经理", "魏秀梅", "800", "13323399527", "lucywei@canic.com.cn"],
#    ["人力资源部", "塔娜", "801", "13920390361", "tana@canic.com.cn"]]
#    write_excel_xls(book_name_xls,0,value_title,sheet_name_xls_00,sheet_name_xls_01,sheet_name_xls_02)

    #创建空xls文件
#    write_excel_xls(book_name_xls, sheet_name_xls_00, sheet_name_xls_01, sheet_name_xls_02)
vaule_append = [["财务部", "周志坚", "802", "13920497297", "zhouzj@canic.com.cn"],
 ["财务部", "李惠言", "803", "13602071056", "lihy@canic.com.cn"]]
read_excle_xls(book_name_xls,sheet_name_xls_00)
write_excel_xlx_append(book_name_xls,vaule_append,sheet_name_xls_00)
read_excle_xls(book_name_xls,sheet_name_xls_00)






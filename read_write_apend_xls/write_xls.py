import xlrd
from xlutils.copy import copy


class Write_excel_xls_append(object):
    def __init__(self, path, value, sheet_name):
        self.path = path
        self.value = value
        self.sheet_name = sheet_name

    def write_excel_xls_append(self):
        """向xls文件内写入（追加）内容"""

        # 写入内容格式[[], [],[]..]
        # 写入内容行数
        index = len(self.value)
        # 读模式打开文件
        work_book = xlrd.open_workbook(self.path)
        # 定位sheet页
        work_sheet = work_book.sheet_by_name(self.sheet_name)
        # sheet页数据行数
        rows_old = work_sheet.nrows
        rows = lambda x: x-1 if x else 0
        row_old_real = rows(rows_old)
        print('原sheet页数据行数为: %s' % (row_old_real))
        # 将读模式转换为写模式
        new_work_book = copy(work_book)
        # 重新定位sheet页
        sheet_num = new_work_book.sheet_index(self.sheet_name)
        new_work_sheet = new_work_book.get_sheet(sheet_num)
        # 追加内容
        for i in range(0, index):
            for j in range(0, len(self.value[i])):
                new_work_sheet.write(rows_old + i, j, self.value[i][j])
        print('写入完成，%s页数据行数为: %s' % (self.sheet_name, rows_old + index))
        # 保存文件
        new_work_book.save(self.path)
        print('新数据保存成功')

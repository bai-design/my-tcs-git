import openpyxl


class Read_excle_xlsx(object):
    def __init__(self, path, sheet_name):
        self.path = path
        self.sheet_name = sheet_name

    # 按sheet页名称读取内容
    def read_excle_xlsx(self):
        # 按sheet页页码读取内容
        """读取xls文件某sheet页内容"""
        work_book = openpyxl.load_workbook(self.path)
        sheets = work_book.sheetnames
        print('打印已有sheet页名称')
        for index, value in enumerate(sheets):
            print("第%s页名称: %s" % (index + 1, value))
        # sheet页页码
        # worksheet = work_book.sheet_by_index(sheet_num)
        # sheet页名称
        worksheet = work_book[self.sheet_name]
        # 读取sheet页内容
        # 判断sheet页内容是否为空
        if worksheet.rows:
            print('读取%s页内容' % self.sheet_name)
            for row in worksheet.rows:
                for cell in row:
                    # 逐行逐列读取数据
                    print(cell.value, "\t", end='')
                print()
        else:
            print('%s页内容为空' % self.sheet_name)

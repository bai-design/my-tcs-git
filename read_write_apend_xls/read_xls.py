import xlrd

class Read_excle_xls(object):
    def __init__(self, path, sheet_name):
        self.path = path
        self.sheet_name = sheet_name

    # 按sheet页名称读取内容
    def read_excle_xls(self):
        # 按sheet页页码读取内容
        """读取xls文件某sheet页内容"""
        work_book = xlrd.open_workbook(self.path)
        sheets = work_book.sheet_names()
        print('打印已有sheet页名称')
        for index, value in enumerate(sheets):
            print("第%s页名称: %s" % (index + 1, value))
        # sheet页页码
        # worksheet = work_book.sheet_by_index(sheet_num)
        # sheet页名称
        worksheet = work_book.sheet_by_name(self.sheet_name)
        # 读取sheet页内容
        # 判断sheet页内容是否为空
        if worksheet.nrows:
            print('读取%s页内容' % self.sheet_name)
            for i in range(0, worksheet.nrows):
                for j in range(0, worksheet.ncols):
                    # 逐行逐列读取数据
                    print(worksheet.cell_value(i, j), "\t", end='')
                print()
        else:
            print('%s页内容为空' % self.sheet_name)
    def read_excle_rows_xls(self):
        # 按sheet页页码读取内容
        """读取xls文件某sheet页内容"""
        work_book = xlrd.open_workbook(self.path)
        # sheets = work_book.sheet_names()
        # sheet页页码
        # worksheet = work_book.sheet_by_index(sheet_num)
        # sheet页名称
        worksheet = work_book.sheet_by_name(self.sheet_name)
        # 将sheet页内容存入字典
        # 判断sheet页内容是否为空
        nsrow = {}
        if worksheet.nrows:
            print('将%s页内容存入字典' % self.sheet_name)
            for i in range(0, worksheet.nrows):
                lscol = []
                for j in range(0, worksheet.ncols):
                    # 逐行逐列读取数据
                    lscol.append(worksheet.cell_value(i, j))
                nsrow[str(i)] = lscol
        else:
            print('%s页内容为空' % self.sheet_name)
        return nsrow
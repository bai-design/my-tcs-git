import xlwt


class Create_excel_xls(object):
    """"""

    def __init__(self, path, *sheet_names):
        self.path = path
        self.sheet_names = sheet_names

    def create_excel_xls(self):
        """创建xls文件与sheet页"""
        workbook = xlwt.Workbook()
        for sheet_name in self.sheet_names:
            workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
            workbook.save(self.path)
        print('OK')

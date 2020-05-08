import openpyxl


class Create_excel_xlsx(object):
    """"""

    def __init__(self, path, *sheet_names):
        self.path = path
        self.sheet_names = sheet_names

    def create_excel_xlsx(self):
        """创建xlsx文件与sheet页"""
        workbook = openpyxl.Workbook()
        i = 0
        for sheet_name in self.sheet_names:
            workbook.create_sheet(sheet_name, i)
            i = i+1
            workbook.save(self.path)
        print('OK')

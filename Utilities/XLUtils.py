import openpyexcel as excel


class XLUtils:
    def __init__(self, file1, sheet_name='Sheet1'):
        self.file1 = file1
        self.sheet_name = sheet_name
        self.workbook = excel.load_workbook(file1)
        self.sheet = self.workbook.active

    def get_row_count(self):
        return self.sheet.max_row

    def get_column_count(self):
        return self.sheet.max_column

    def write_data(self, row, column, value):
        self.sheet.cell(row, column).value = value
        self.workbook.save(self.file1)

    def read_data(self,row,column):

        return self.sheet.cell(row,column).value


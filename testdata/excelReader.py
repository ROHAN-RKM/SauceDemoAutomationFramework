import openpyxl

class ExcelReader:

    @staticmethod
    def read_login_data():

        file_path = "testdata/sheet1.xlsx"

        workbook = openpyxl.load_workbook(file_path)

        sheet = workbook["Sheet1"]

        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):

            Username = row[0]
            Password = row[1]
            Expected = row[2]

            data.append((Username, Password, Expected))

        return data
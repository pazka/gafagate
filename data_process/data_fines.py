from data_process.data_helper import DataHelper
from datetime import date
from openpyxl import Workbook
from openpyxl.cell import Cell
from data_process.data_helper import DataHelper, DataDate, DataPoint


class FinesData(DataHelper):
    def __init__(self, wb: Workbook):
        self.data = []

        sheet = wb["Fines"]
        raw_data: list[list[Cell]] = sheet["B2:B75"]

        month = 4
        year = 2018
        for data in raw_data:
            if data[0].value is None:
                self.data.append((date(year, month, 1), 0))
            else:
                self.data.append((date(year, month, 1), float(data[0].value)))

            month += 1
            if month > 12:
                month = 1
                year += 1

        super().__init__(self.data)
        self.filter_dates(date(2019, 1, 1), date(2023, 12, 31))
        self.clamp_values(0, 100*1000*1000)

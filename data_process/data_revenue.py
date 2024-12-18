from data_process.data_helper import DataHelper
from datetime import date
from openpyxl import Workbook
from openpyxl.cell import Cell
from data_process.data_helper import DataHelper, DataDate, DataPoint


class RevenueData(DataHelper):
    def __init__(self, wb: Workbook):
        sheet = wb["Revenue"]
        # yearly data from 2011 to 2023
        raw_data: list[list[Cell]] = sheet["G2:G14"]
        yearly_data: list[DataPoint] = []

        for i, data in enumerate(raw_data):
            if type(data[0].value) == str:
                value = float(data[0].value.replace(",", ""))
            else:
                value = data[0].value

            yearly_data.append((date(2011+i, 1, 1), value))

        monthly_data: list[DataPoint] = []
        for year_data in yearly_data:
            year = year_data[0].year
            revenue = year_data[1]
            month_revenue = revenue/12

            for j in range(1, 13):
                monthly_data.append((date(year, j, 1), month_revenue * j))

        super().__init__(monthly_data)
        self.filter_dates(date(2019, 1, 1), date(2023, 12, 31))

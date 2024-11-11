from data_process.data_helper import DataHelper
from datetime import date
from openpyxl import Workbook
from openpyxl.cell import Cell
from data_process.data_helper import DataHelper, DataDate, DataPoint


class InflationData(DataHelper):
    def __init__(self, wb: Workbook):
        sheet = wb["Inflation"]
        # yearly data from 2011 to 2023
        raw_data: list[list[Cell]] = sheet["B3:B16"]
        yearly_data: list[DataPoint] = []

        for i, data in enumerate(raw_data):
            if type(data[0].value) == str:
                value = float(data[0].value.replace("%", ""))
            else:
                value = data[0].value
            value = value * 100
            yearly_data.append((date(2010+i, 1, 1), value))

        monthly_data: list[DataPoint] = []
        year_data = (date(2009, 1, 1), 0)
        for i in range(0, len(yearly_data)):
            year_data = yearly_data[i-1]
            next_year_data = yearly_data[i]

            year = year_data[0].year
            inflation = year_data[1]
            next_inflation = next_year_data[1]

            month_inflation = (next_inflation-inflation)/12

            for j in range(1, 13):
                monthly_data.append(
                    (date(year, j, 1), inflation+(month_inflation * j)))

        super().__init__(monthly_data)
        self.filter_dates(date(2019, 1, 1), date(2023, 12, 31))

from data_process.data_helper import DataHelper
from datetime import date
from openpyxl import Workbook
from data_helper import DataHelper, DataDate, DataPoint


class RevenueData(DataHelper):
    def __init__(self, wb: Workbook):
        sheet = wb["data_revenue"]
        # yearly data from 2011 to 2023
        raw_data: list[DataPoint] = sheet["G2:G14"]
        yearly_data: list[DataPoint] = []

        for i in range(0, len(raw_data)):
            yearly_data = (date(2011+i, 1, 1), raw_data[i])

        monthly_data: list[DataPoint] = []
        for i in range(0, len(yearly_data-1)):
            revenue_delta = yearly_data[i+1][1] - yearly_data[i][1]
            year = yearly_data[i][0].year

            for j in range(1, 12):
                monthly_data.push((date(year, j, 1), revenue_delta * (j/12)))

        super().__init__(monthly_data)
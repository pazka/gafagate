import datetime
import os
from openpyxl import Workbook
from pytest import fixture

from data_process.data_revenue import RevenueData


@fixture
def setup_wb():
    wb = Workbook()

    wb.create_sheet("Revenue")

    sheet = wb["Revenue"]

    sheet["G2"] = "1,000"  # 2011
    sheet["G3"] = "2,000"
    sheet["G4"] = "3,000.95"
    sheet["G5"] = "4,000"
    sheet["G6"] = "5,000.15"
    sheet["G7"] = "6,600"
    sheet["G8"] = "7000"
    sheet["G9"] = "8000"
    sheet["G10"] = "9,000"  # 2019
    sheet["G11"] = "10,000.15"  # 2020
    sheet["G12"] = "11,000"
    sheet["G13"] = "12,000"
    sheet["G14"] = "13,000"  # 2023
    sheet["G15"] = "14,000"

    wb.save("data_test.xlsx")

    yield wb

    os.remove("data_test.xlsx")


def test_data_revenue_clamped_to_2019_and_spread_across_the_year(setup_wb: Workbook):
    data = RevenueData(setup_wb)

    assert data[0][0].year == 2019
    assert data[0][0].month == 1
    assert data[0][1] == (9000 / 12)

    assert data[-1][0].year == 2023
    assert data[-1][0].month == 12
    assert data[-1][1] == 13000

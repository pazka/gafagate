import datetime
import os
from openpyxl import Workbook
from pytest import fixture

from data_process.data_revenue import RevenueData


@fixture
def setup_wb():
    wb = Workbook()

    wb.create_sheet("data_revenue")

    sheet = wb["data_revenue"]

    sheet["G2"] = 1000  # 2011
    sheet["G3"] = 2000
    sheet["G4"] = 3000
    sheet["G5"] = 4000
    sheet["G6"] = 5000
    sheet["G7"] = 6000
    sheet["G8"] = 7000
    sheet["G9"] = 8000
    sheet["G10"] = 9000  # 2019
    sheet["G11"] = 10000  # 2020
    sheet["G12"] = 11000
    sheet["G13"] = 12000
    sheet["G14"] = 13000  # 2023
    sheet["G15"] = 14000

    wb.save("data_test.xlsx")

    yield wb

    os.remove("data_test.xlsx")


def test_data_revenue_clamped_to_2019_and_spread_across_the_year(setup_wb: Workbook):
    data = RevenueData(setup_wb)
    sheet = setup_wb["data_revenue"]

    assert data[0][0].year == 2019
    assert data[0][0].month == 1
    assert data[0][1] == sheet["G10"].value / 12

    assert data[-1][0].year == 2023
    assert data[-1][0].month == 12
    assert data[-1][1] == sheet["G14"].value

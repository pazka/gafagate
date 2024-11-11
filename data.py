from time import sleep
from PyDMXControl.controllers import OpenDMXController
from StairvilleFixture import StairvilleFixture
from openpyxl import Workbook
from ChauvetFixture import ChauvetFixture
from data_process.data_revenue import RevenueData


dmx = OpenDMXController()

fixture = dmx.add_fixture(
    StairvilleFixture, name="StairvilleFixture-2", start_channel=10)

fixture2 = dmx.add_fixture(
    ChauvetFixture, name="ChauvetFixture", start_channel=1, mode=9)

wb = Workbook("./data.xlsx")
revenue_data = RevenueData(wb)


while True:
    for data_point in revenue_data:
        fixture.color([data_point[1], 0, 0, 0], 1)
        fixture2.simple_color([data_point[1], 0, 0, 0])
        sleep(1)

dmx.close()

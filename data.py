from time import sleep
import os
from PyDMXControl.controllers import OpenDMXController
from fixtures.StairvilleFixture import StairvilleFixture
from openpyxl import Workbook, load_workbook
from fixtures.ChauvetFixture import ChauvetFixture
from data_process.data_revenue import RevenueData


dmx = OpenDMXController()

fixture: StairvilleFixture = dmx.add_fixture(
    StairvilleFixture, name="StairvilleFixture-2", start_channel=10)

fixture2: ChauvetFixture = dmx.add_fixture(
    ChauvetFixture, name="ChauvetFixture", start_channel=1, mode=9)

# os test that file exists

if os.path.exists("data/data.xlsx"):
    print("File exists")
else:
    print("File does not exist")


wb = load_workbook(filename="data/data.xlsx", read_only=True, data_only=True)
revenue_data = RevenueData(wb)


while True:
    for data_point in revenue_data:
        uv = revenue_data.to_uv(data_point[1])
        fixture.simple_color([uv*255, 0, 0, 0], 1)
        fixture2.simple_color([uv*255, 0, 0])
        sleep(1)

dmx.close()

from time import sleep
import os
from PyDMXControl.controllers import OpenDMXController
from fixtures.StairvilleFixture import StairvilleFixture
from openpyxl import Workbook, load_workbook
from fixtures.ChauvetFixture import ChauvetFixture
from data_process.data_revenue import RevenueData
from data_process.data_fines import FinesData
from helpers import normalize,interpolate
from data_process.data_inflation import InflationData

dmx = OpenDMXController()

fixture1: StairvilleFixture = dmx.add_fixture(
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
fines_data = FinesData(wb)
inflation_data = InflationData(wb)
wb.close()

fixture1.dim(255, 1/200)
fixture2.dim(255, 1)

dim_speed = 0.01
color_transition_time = 1

while True:
    prev_color = (0, 0, 0)
    for i in range(0, len(revenue_data)):
        revenue_data_point = revenue_data[i]
        fines_data_point = fines_data[i]
        inflation_data_point = inflation_data[i]

        new_color_uv = (
            revenue_data.to_uv(revenue_data_point) * 255,
            fines_data.to_uv(fines_data_point) * 255,
            inflation_data.to_uv(inflation_data_point) * 255
        )

        print("-------------------------------")
        print("Date : ", revenue_data_point[0])
        print("GAFAM Revenue (millions) : ", round(
            revenue_data_point[1]))
        print("GDPR Fines (millions): ", round(
            fines_data_point[1]/1000000))
        print("OECD members Rate %: ", round(inflation_data_point[1], 2))
        print("Color (R,G,B): ", (round(new_color_uv[0]), round(new_color_uv[1]), round(new_color_uv[2])))
        # display next color gradually
        counter = 0
        while counter < color_transition_time:
            counter += dim_speed
            # TODO : fix : interpoation sometimes give negative values
            transition_color = interpolate(prev_color, new_color_uv, counter / color_transition_time)
            #print("Transition Color (R,G,B): ", (round(transition_color[0]), round(transition_color[1]), round(transition_color[2])))
            fixture1.simple_color(transition_color)
            fixture2.simple_color(transition_color)
            sleep(dim_speed)

        prev_color = new_color_uv

dmx.close()

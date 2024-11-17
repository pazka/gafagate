#!/home/pazka/gafagate-env/bin/python -u
import math
from time import sleep
import os
from PyDMXControl.controllers import OpenDMXController
from fixtures.StairvilleFixture import StairvilleFixture
from openpyxl import Workbook, load_workbook
from fixtures.ChauvetFixture import ChauvetFixture
from data_process.data_revenue import RevenueData
from data_process.data_fines import FinesData
from helpers import normalize, interpolate, extract_1_from_color
from data_process.data_inflation import InflationData
from plot import update_plot, update_plot_non_blocking

success_init = False

while not success_init:
    try:
        dmx = OpenDMXController()
        success_init = True
    except Exception as e:
        print("Error: ", e)
        print("Waiting for USB UART FTI dmx controller ", e)
        sleep(5)

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

fixture1.dim(255)
fixture2.dim(255)
fixture2.set_channel('dimmer_speed', 53)

dim_speed = 0.05
dim_steps = 30


def display_color(color):
    fixture2.color(color, )
    fixture1.color(color, )


def gradient_from_to(from_color: tuple[int, int, int], to_color: tuple[int, int, int], steps):
    if steps < 3:
        steps = 3
    for i in range(0, int(steps/3)):
        yield from_color
        update_plot_non_blocking(from_color[0], from_color[1], from_color[2])
    for i in range(0, int(steps/3)):
        c = interpolate(from_color, to_color, i / int(steps/3))
        update_plot_non_blocking(c[0], c[1], c[2])
        yield c
    for i in range(0, int(steps/3)):
        update_plot_non_blocking(to_color[0], to_color[1], to_color[2])
        yield to_color


while True:
    prev_color = (0, 0, 0)
    for i in range(0, len(revenue_data)):
        revenue_data_point = revenue_data[i]
        fines_data_point = fines_data[i]
        inflation_data_point = inflation_data[i]

        new_color_uv = (
            math.ceil(revenue_data.to_uv(revenue_data_point) * 255),
            math.ceil(fines_data.to_uv(fines_data_point) * 255),
            math.ceil(inflation_data.to_uv(inflation_data_point) * 255)
        )

        print("-------------------------------")
        print("RED: ", new_color_uv[0])

        for display_color in gradient_from_to(extract_1_from_color(prev_color, 2), extract_1_from_color(new_color_uv, 0), dim_steps):
            fixture1.simple_color(display_color)
            fixture2.simple_color(display_color)
            sleep(dim_speed)

        print("GREEN: ", new_color_uv[1])
        for display_color in gradient_from_to(extract_1_from_color(new_color_uv, 0), extract_1_from_color(new_color_uv, 1), dim_steps):
            fixture1.simple_color(display_color)
            fixture2.simple_color(display_color)
            sleep(dim_speed)

        print("BLUE: ", new_color_uv[2])
        for display_color in gradient_from_to(extract_1_from_color(new_color_uv, 1), extract_1_from_color(new_color_uv, 2), dim_steps):
            fixture1.simple_color(display_color)
            fixture2.simple_color(display_color)
            sleep(dim_speed)

        prev_color = new_color_uv


dmx.close()

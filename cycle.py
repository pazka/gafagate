from time import sleep
from PyDMXControl.controllers import OpenDMXController
from fixtures.StairvilleFixture import StairvilleFixture
from openpyxl import Workbook
from fixtures.ChauvetFixture import ChauvetFixture
from cycle import fixture


dmx = OpenDMXController()
fixture = dmx.add_fixture(StairvilleFixture, name="StairvilleFixture-1")

colors = [[255, 0, 0, 0], [0, 255, 0, 0], [0, 0, 255, 0]]

fixture.dim(255, 1)

while True:
    for color in colors:
        print("color :", color)
        fixture.color(color, 1)
        sleep(1)

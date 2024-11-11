from time import sleep
from PyDMXControl.controllers import OpenDMXController
from fixtures.StairvilleFixture import StairvilleFixture
from openpyxl import Workbook
from fixtures.ChauvetFixture import ChauvetFixture


dmx = OpenDMXController()
fix: StairvilleFixture = dmx.add_fixture(
    StairvilleFixture, name="StairvilleFixture-2", start_channel=10)

fix1: ChauvetFixture = dmx.add_fixture(
    ChauvetFixture, name="ChauvetFixture", start_channel=1, mode=9)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

fix.dim(255, 1)
fix1.dim(255, 1)

while True:
    for color in colors:
        print("color :", color)
        fix.simple_color(color)
        fix1.simple_color(color)
        sleep(0.001)

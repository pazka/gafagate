from time import sleep
from PyDMXControl.controllers import OpenDMXController
from StairvilleFixture import StairvilleFixture
from openpyxl import Workbook
from ChauvetFixture import ChauvetFixture


dmx = OpenDMXController()
fixture = dmx.add_fixture(StairvilleFixture, name="StairvilleFixture-1")

colors = [[255,0,0,0],[0,255,0,0],[0,0,255,0]]

fixture.dim(255,1)

while True:
    for color in colors:
        print("color :",color)
        fixture.color(color,1)
        sleep(1)
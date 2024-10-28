from PyDMXControl.controllers import OpenDMXController
from StairvilleFixture import StairvilleFixture
from openpyxl import Workbook


dmx = OpenDMXController()
fixture = dmx.add_fixture(StairvilleFixture, name="StairvilleFixture")
dmx.web_control()

# Once the console debug mode is exited the script will continue, to stop it
#  exiting and stopping DMX output when can use a built-in sleep function.
# This sleep function will wait until enter is pressed in the console before continuing.
dmx.sleep_till_enter()

dmx.close()
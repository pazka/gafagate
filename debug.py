from PyDMXControl.controllers import OpenDMXController
from StairvilleFixture import StairvilleFixture
from openpyxl import Workbook
from ChauvetFixture import ChauvetFixture


dmx = OpenDMXController()
fixture = dmx.add_fixture(StairvilleFixture, name="StairvilleFixture-2",start_channel=10)
fixture2 = dmx.add_fixture(ChauvetFixture, name="ChauvetFixture",start_channel=1,mode=9)


dmx.web_control()

# Once the console debug mode is exited the script will continue, to stop it
#  exiting and stopping DMX output when can use a built-in sleep function.
# This sleep function will wait until enter is pressed in the console before continuing.
dmx.sleep_till_enter()
dmx.close()
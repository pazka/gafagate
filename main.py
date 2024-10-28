from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import RGB_Vdim
from StairvilleFixture import StairvilleFixture

dmx = OpenDMXController()
fixture = dmx.add_fixture(StairvilleFixture, name="StairvilleFixture")
dmx.web_control()


dmx.close()
"""
Stairville 132 LED RGB DMX
1 put in 6ch mode

|channel|val|function|
|---|---|---|
|1|0-255|Dimmer (0 to 100%)|
|2|0-5| LEDS on, brightness controlled by channel 1|
|2|6-10| LEDS off, blackout|
|2|11-33| Strobe - Random impulses, increasing speed|
|2|34-56| Strobe - Random increasing brightness, increasing speed|
|2|57-79| Strobe - Random decreasing brightness, increasing speed|
|2|80-102| Strobe - Random strobe effect, increasing speed|
|2|103-127| Interrupt effect 5s to 1s|
|2|128-250| Strobe - strobe effect, speed increasing from approx. 0hz to 30hz|
|2|251-255| LEDs on, brightness controlled by channel 1|
|3|0-255| Red (0 to 100%)|
|4|0-255| Green (0 to 100%)|
|5|0-255| Blue (0 to 100%)|
|6|0-5| Sound control OFF |
|6|6-255| Sound control ON increasing sensitivity|
"""

from PyDMXControl.profiles.defaults import Fixture


class StairvilleFixture(Fixture):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._register_channel('dimmer')
        self._register_channel_aliases('dimmer', 'dim')
        self._register_channel('Strobe')
        self._register_channel_aliases('strobe', 'st')
        self._register_channel('red')
        self._register_channel_aliases('red', 'r')
        self._register_channel('green')
        self._register_channel_aliases('green', 'g')
        self._register_channel('blue')
        self._register_channel_aliases('blue', 'b')
        self._register_channel('sound')
        self._register_channel_aliases('sound', 'so')

    def simple_color(self, color: tuple[int, int, int]):
        self.color([color[0], color[1], color[2], 0], 1)

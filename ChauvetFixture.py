"""
Chauvet Core PAR Q120 ILS RGW

https://www.chauvetdj.com/wp-content/uploads/2022/06/COREpar_Q120_ILS_UM_Rev1.pdf

| 4-Ch Mode  || 9-Ch mode  | Function                         | Value           | Percent/Setting                |
|-----||-----|----------------------------------|-----------------|---------------------------------------------|
| 1   || 1   | Red                              | 000 - 255       | 0-100%                                      |
| 2   || 2   | Green                            | 000 - 255       | 0-100%                                      |
| 3   || 3   | Blue                             | 000 - 255       | 0-100%                                      |
| 4   || 4   | White                            | 000 - 255       | 0-100%                                      |
|-----||-----|----------------------------------|-----------------|---------------------------------------------|
| -   || 5   | Color macros                     | 000 - 010       | No function                                 |
|     || 5   |                                  | 011 - 255       | Color macros                                |
| -   || 6   | Strobe (when Ch. 7 is 000-031)   | 000 - 015       | No function                                 |
|     || 6   |                                  | 016 - 255       | Strobe (slow to fast)                       |
| -   || 6   | Program speed (when Ch. 7 is 032-223) | 000 - 255 | Program speed, slow to fast                 |
| -   || 6   | Sound sensitivity (when Ch. 7 is 224-255) | 000 - 010 | Sound sensitivity off                      |
|     || 6   |                                  | 011 - 255       | Sound sensitivity, low to high              |
| -   || 7   | Auto program                     | 000 - 031       | No function                                 |
|     || 7   |                                  | 032 - 063       | Pulse effect, 0-100% (when Ch. 1-4 are active) |
|     || 7   |                                  | 064 - 095       | Pulse effect, 100-0% (when Ch. 1-4 are active) |
|     || 7   |                                  | 096 - 127       | Pulse effect, 100-0-100% (when Ch. 1-4 are active) |
|     || 7   |                                  | 128 - 159       | Automatic 4-color pulse                     |
|     || 7   |                                  | 160 - 191       | Automatic 4-color snap                      |
|     || 7   |                                  | 192 - 223       | Automatic 29-color snap                     |
|     || 7   |                                  | 224 - 255       | Sound-active 29-color snap                  |
| -   || 8   | Dimmer                           | 000 - 255       | 0-100%                                      |
| -   || 9   | Dimmer speed                     | 000 - 051       | Dimmer speed set from display menu          |
|     || 9   |                                  | 052 - 101       | Dimmer speed mode off                       |
|     || 9   |                                  | 102 - 152       | Dimmer speed mode 1 (fast)                  |
|     || 9   |                                  | 153 - 203       | Dimmer speed mode 2 (medium)                |
|     || 9   |                                  | 204 - 255       | Dimmer speed mode 3 (slow)                  |

"""

from PyDMXControl.profiles.defaults import Fixture


class ChauvetFixture(Fixture):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # get mode from args
        self.mode = kwargs.get('mode', 4)

        if self.mode == 4:
            self._register_channel('red')
            self._register_channel_aliases('red', 'r')
            self._register_channel('green')
            self._register_channel_aliases('green', 'g')
            self._register_channel('blue')
            self._register_channel_aliases('blue', 'b')
            self._register_channel('white')
            self._register_channel_aliases('white', 'w')
        elif self.mode == 9:
            self._register_channel('red')
            self._register_channel_aliases('red', 'r')
            self._register_channel('green')
            self._register_channel_aliases('green', 'g')
            self._register_channel('blue')
            self._register_channel_aliases('blue', 'b')
            self._register_channel('white')
            self._register_channel_aliases('white', 'w')
            self._register_channel('color_macros')
            self._register_channel_aliases('color_macros', 'cm')
            self._register_channel('strobe')
            self._register_channel_aliases('strobe', 'st')
            self._register_channel('auto_program')
            self._register_channel_aliases('auto_program', 'ap')
            self._register_channel('dimmer')
            self._register_channel_aliases('dimmer', 'dim')
            self._register_channel('dimmer_speed')
            self._register_channel_aliases('dimmer_speed', 'ds')

    def simple_color(self, color: tuple[int, int, int, int]):
        if self.mode == 4:
            self.color([color[0], color[1], color[2], color[3]], 1)
        elif self.mode == 9:
            self.color([color[0], color[1], color[2],
                       color[3], 0, 0, 0, 0, 0], 1)

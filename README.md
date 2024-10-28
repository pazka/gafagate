# test lighting

## Troubleshooting

### Trouble 1

`name must not be empty`

### Solution 1

`pip install --force-reinstall flask==2.2.4`

### Trouble 2

`No backend available`

### Solution 2

>Good news -- in stepping through the installation for pyftdi (<https://eblot.github.io/pyftdi/installation.html>), simply following the instructions for Zadig to replace the driver for the USB device (i.e. ultraDMX Micro) allowed dmx = OpenDMXController() to work without the "backend" error. So it appears I can begin to mess around with PyDMXControl.

- Install software from <https://github.com/pbatard/libwdi/releases/download/v1.5.1/zadig-2.9.exe>

- Search for UART or FTDI device
- Replace driver with libusb-win32 (v1.4.0.0) because it's what the project supports

### Trouble 3

`erial.serialutil.SerialException: Cannot configure port, something went wrong. Original message: PermissionError(13, 'A device attached to the system is not functioning.', None, 31)`

### Solution 3

<https://ftdichip.com/drivers/vcp-drivers/>

## LED Hardware

3 Stairville 132 LED RGB DMX
1 put in 6ch mode
2 in slave mode

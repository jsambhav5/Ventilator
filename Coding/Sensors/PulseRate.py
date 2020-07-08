#!/usr/bin/python3
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

PR = 7

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


print('Reading MCP3008 values, press Ctrl-C to quit...')
while True:
    value = mcp.read_adc(PR)
    print(value)
    # Pause for half a second.
    time.sleep(0.5)
# Code adapted from: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

y_axis = analogio.AnalogIn(board.GP27)
x_axis = analogio.AnalogIn(board.GP26)
select = digitalio.DigitalInOut(board.GP16)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def steps(axis):
    """ Maps the potentiometer voltage range to 0-20 """
    return round((axis - pot_min) / step)

while True:
    x_steps = steps(get_voltage(x_axis))
    y_steps = steps(get_voltage(y_axis))

    if not select.value:
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.2)  # Debounce delay

    if x_steps > 19.0:
        mouse.move(x=8)
    if x_steps > 11.0:
        mouse.move(x=1)
    if x_steps < 9.0:
        mouse.move(x=-1)
    if x_steps < 8.0:
        mouse.move(x=-8)

    if y_steps > 19.0:
        mouse.move(y=-8)
    if y_steps > 11.0:
        mouse.move(y=-1)
    if y_steps < 9.0:
        mouse.move(y=1)
    if y_steps < 1.0:
        mouse.move(y=8)


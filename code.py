print("Starting")

import board
import busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from kmk.modules.macros import Macros
from kmk.modules.layers import Layers
from adafruit_display_text import label
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,)
keyboard.col_pins = (board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,)

keyboard.modules.append(Layers())

WOW = KC.MACRO("A new terror born in death, a new superstition entering the unassailable fortress of forever.I am legend.")
LAYER_T1 = KC.TO(0) 
LAYER_T2 = KC.TO(1) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.ESC,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,   KC.N9,    KC.N0,       KC.MINUS,    KC.BSPC,
        KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,    KC.O,     KC.P,        KC.LBRACKET, KC.RBRACKET,
        KC.BSLASH, KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,    KC.L,     KC.SCOLON,   KC.QUOTE,    KC.ENTER,
        KC.LSHIFT, KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM, KC.DOT,   KC.SLSH,     KC.UP,       KC.RSHIFT,
        KC.LCTL,   KC.LGUI,  KC.LALT,  KC.SPC,   KC.SPC,   KC.SPC,   WOW,      LAYER_T2, KC.RALT, KC.EQUAL, KC.LEFT,     KC.DOWN,     KC.RIGHT,
    ],
    [
        KC.ESC,    KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,   KC.F9,   KC.F10,      KC.F11,      KC.F12,
        KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,    KC.O,    KC.P,        KC.LBRACKET, KC.RBRACKET,
        KC.BSLASH, KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,    KC.L,    KC.SCOLON,   KC.QUOTE,    KC.ENTER,
        KC.LSHIFT, KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM, KC.DOT,  KC.SLSH,     KC.UP,       KC.RSHIFT,
        KC.LCTL,   KC.LGUI,  KC.LALT,  KC.SPC,   KC.SPC,   KC.SPC,   KC.SPC,   LAYER_T1, KC.RALT, KC.PSCR, KC.HOME,     KC.DOWN,     KC.END,
    ],

]

#
#keyboard.keymap = [
#    [KC.A,]
#]

if __name__ == '__main__':
    keyboard.go()

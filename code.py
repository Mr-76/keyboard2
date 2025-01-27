print("Starting")

import board

from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.col_pins = (board.GP10,board.GP11,board.GP12,)
keyboard.row_pins = (board.GP15,board.GP14,board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
LAYER_TAP = KC.TO(1) # any tap longer than 250ms will be interpreted as a hold
LAYER_TAP2 = KC.TO(0) # any tap longer than 250ms will be interpreted as a hold


keyboard.keymap = [
    # Function Layer
	[
		KC.F1,	KC.F2,	KC.F3,
		KC.F4,	KC.F5,	KC.F6,
		KC.F7,  KC.F8,  LAYER_TAP,	
	],
    [
        KC.A,KC.B,KC.C,
        KC.D,KC.E,KC.F,
        KC.G,KC.H,LAYER_TAP2,
    ],
]

if __name__ == '__main__':
    keyboard.go()


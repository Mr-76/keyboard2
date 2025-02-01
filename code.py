print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()



keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,)
keyboard.col_pins = (board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP17,board.GP18,board.GP19,board.GP20,board.GP21,)


#keyboard.col_pins = (board.GP5,)
#keyboard.row_pins = (board.GP0,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    # Function Layer
    [
        KC.ESC,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,   KC.N9,   KC.N0,       KC.MINUS,    KC.BSPC,
        KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,    KC.O,    KC.P,        KC.LBRACKET, KC.RBRACKET,
        KC.BSLASH, KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,    KC.L,    KC.SCOLON,   KC.QUOTE,    KC.ENTER,
        KC.LSHIFT, KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM, KC.DOT,  KC.SLSH,     KC.UP,       KC.RSHIFT,
        KC.LCTL,   KC.LGUI,  KC.LALT,  KC.SPC,   KC.SPC,   KC.SPC,   KC.SPC,   KC.SPC,   KC.RALT, KC.PSCR, KC.LEFT,     KC.DOWN,     KC.RIGHT,
    ]

]

#
#keyboard.keymap = [
#    [KC.A,]
#]

if __name__ == '__main__':
    keyboard.go()

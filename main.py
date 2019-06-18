from pyb import *
BLUE = Pin.board.D7

def pin_toggler(p):
    Pin.pinMode(p, Pin.OUTPUT)
    val = False
    def toggle():
        nonlocal val
        val = not val
        Pin.digitalWrite(p, Pin.HIGH if val else Pin.LOW)
    return toggle

toggle_led = pin_toggler(BLUE)
del BLUE

# Write your code here :-)
# Write your code here :-)
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value
    Level=[10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000]
    print(volume)

    LedOn=0
    for i, Level in enumerate(Level):
        if volume>=Level:
            LedOn=i+1
        for i, led in enumerate(leds):
            led.value=i<LedOn

    sleep(0.001)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?


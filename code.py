import time
import board
import touchio
from digitalio import DigitalInOut, Direction



touch_A2 = touchio.TouchIn(board.A2)

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
    print("use adafruit_dotstar")
else:
    import neopixel
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)
    print("use neopixel")

led.brightness = 0.3
flag = False
now = time.monotonic() # monotonic() is the real time function regardless of sleep()
while True:
    if led[0]==(0,0,0) and not touch_A2.value:
        continue
    elif led[0]==(0,0,0) and touch_A2.value:
        led[0] = (255, 0, 0)
        print("Touched A2!")
        now = time.monotonic()
        time.sleep(0.2) # give time for hand to leave

    elif time.monotonic()-now < 2:
        if touch_A2.value:
            print("touch a2")
            now = time.monotonic()
            led[0] = (255, 0, 0)
            time.sleep(0.5)
            led[0] = (0, 255, 0)
            time.sleep(0.5)
            led[0] = (0, 0, 255)
            time.sleep(0.5)
            flag = True
        elif flag == True:
            print("previous second touched")
            led[0] = (255, 0, 0)
            time.sleep(0.5)
            led[0] = (0, 255, 0)
            time.sleep(0.5)
            led[0] = (0, 0, 255)
            time.sleep(0.5)
            flag = False
        else:
            print("only the first touch")
            led[0] = (255,0,0)

    else:
        led[0]=(0,0,0)

import gpiod
import sys
import time

try:
    if len(sys.argv) > 2:
        LED_CHIP = sys.argv[1]
        LED_LINE_OFFSETS = []
        for i in range(len(sys.argv) - 2):
            LED_LINE_OFFSETS.append(int(sys.argv[i + 2]))
    else:
        raise Exception()
except:
    print(
        "Usage:"
        + "    python3 -m gpiod.test.bulk_blink <chip> <line offset1>"
        + " [<line offset2> ...]"
    )
    sys.exit()

chip = gpiod.chip(LED_CHIP)
leds = chip.get_lines(LED_LINE_OFFSETS)

config = gpiod.line_request()
config.consumer = "Bulk Blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

leds.request(config)

off = [0] * leds.size
on = [1] * leds.size

while True:
    leds.set_values(off)
    time.sleep(0.1)
    leds.set_values(on)
    time.sleep(0.1)

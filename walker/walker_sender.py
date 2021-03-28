running_time_in_seconds = 0
radio.set_transmit_power(7)
originalgroup = 2
radio.set_group(originalgroup)
radio.send_string("Initialising")
basic.pause(500)

def on_forever():
    global running_time_in_seconds
    running_time_in_seconds = Math.round(input.running_time()) / 1000
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    basic.pause(200)
    radio.send_number(0)
basic.forever(on_forever2)

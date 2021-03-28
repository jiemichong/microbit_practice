def on_received_string(receivedString):
    if receivedString == "Moving":
        basic.show_icon(IconNames.DUCK)
    elif receivedString == "Still":
        basic.clear_screen()
radio.on_received_string(on_received_string)

running_time_in_seconds = 0
radio.set_group(1)
number = 1
currenttime = running_time_in_seconds
initialtime = running_time_in_seconds

def on_forever():
    global running_time_in_seconds
    running_time_in_seconds = Math.round(input.running_time()) / 1000
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    basic.pause(200)
    radio.send_number(0)
basic.forever(on_forever2)

def on_forever3():
    radio.set_transmit_power(7)
    radio.send_number(0)
    basic.pause(200)
basic.forever(on_forever3)

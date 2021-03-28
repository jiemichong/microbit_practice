def on_received_number(receivedNumber):
    global day_night
    if receivedNumber >= 0 and receivedNumber <= 100:
        day_night = 0
        if showDN == 1:
            basic.show_string("N")
    else:
        day_night = 1
        if showDN == 1:
            basic.show_string("D")
radio.on_received_number(on_received_number)

def on_received_string(receivedString):
    global help2, last_move_time, inactive
    if receivedString == "Help":
        help2 = 1
    elif receivedString == "Cancel":
        basic.clear_screen()
        help2 = 0
    if receivedString == "Motion Detected":
        last_move_time = running_time_in_secs
        if inactive == 1:
            inactive = 0
            basic.clear_screen()
radio.on_received_string(on_received_string)

running_time_in_secs = 0
help2 = 0
day_night = 0
inactive = 0
last_move_time = 0
showDN = 0
radio.set_transmit_power(7)
radio.set_group(1)
showDN = 1
last_move_time = 0
inactive = 0

def on_forever():
    global showDN
    if help2 == 1:
        showDN = 0
    elif day_night == 0:
        showDN = 1
    if day_night == 1 and inactive == 1:
        showDN = 0
    if help2 == 0 and inactive == 0:
        showDN = 1
basic.forever(on_forever)

def on_forever2():
    if help2 == 1 and inactive == 1 and day_night == 1:
        basic.show_icon(IconNames.NO)
        basic.pause(250)
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.pause(250)
    elif help2 == 1:
        basic.show_icon(IconNames.NO)
    elif inactive == 1 and day_night == 1:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.pause(500)
basic.forever(on_forever2)

def on_forever3():
    global inactive, last_move_time
    if day_night == 0:
        inactive = 0
        last_move_time = running_time_in_secs
    elif running_time_in_secs - last_move_time >= 5:
        inactive = 1
basic.forever(on_forever3)

def on_forever4():
    global running_time_in_secs
    running_time_in_secs = Math.round(input.running_time()) / 1000
    basic.pause(1000)
basic.forever(on_forever4)

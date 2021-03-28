def on_received_number(receivedNumber):
    global currentstrength, initialstrength, initialtime, currenttime
    if initialised == 1:
        currentstrength = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
        if currentstrength != initialstrength and abs(currentstrength - initialstrength) >= 8:
            radio.set_group(1)
            radio.send_string("Moving")
            initialstrength = currentstrength
            initialtime = running_time_in_seconds
            currenttime = running_time_in_seconds
        else:
            currenttime = running_time_in_seconds
            if currenttime - initialtime >= 5:
                radio.set_group(1)
                radio.send_string("Still")
        radio.set_group(originalgroup)
radio.on_received_number(on_received_number)

def on_received_string(receivedString):
    global initialstrength, currentstrength, initialised
    initialstrength = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    currentstrength = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    initialised = 1
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        """)
    basic.pause(300)
    basic.clear_screen()
radio.on_received_string(on_received_string)

initialstrength = 0
currentstrength = 0
initialised = 0
currenttime = 0
running_time_in_seconds = 0
initialtime = 0
originalgroup = 0
originalgroup = 2
radio.set_group(originalgroup)
initialtime = running_time_in_seconds
currenttime = running_time_in_seconds
initialised = 0

def on_forever():
    global running_time_in_seconds
    running_time_in_seconds = Math.round(input.running_time()) / 1000
    basic.pause(1000)
basic.forever(on_forever)

def on_button_pressed_a():
    radio.send_string("Help")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("Cancel")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_string("Motion Detected")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

running_time_in_secs = 0
light2 = 0
radio.set_transmit_power(7)
radio.set_group(1)

def on_forever():
    global light2
    basic.pause(1000)
    light2 = input.light_level()
    radio.send_number(light2)
basic.forever(on_forever)

def on_forever2():
    global running_time_in_secs
    running_time_in_secs = Math.round(input.running_time()) / 1000
    basic.pause(1000)
basic.forever(on_forever2)

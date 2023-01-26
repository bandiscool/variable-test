def on_button_pressed_a():
    global variable_test
    variable_test += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global variable_test
    variable_test = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global variable_test
    variable_test += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

variable_test = 0
variable_test = 0

def on_forever():
    basic.show_number(variable_test)
basic.forever(on_forever)

input.onButtonPressed(Button.A, function () {
    variable_test += 1
})
input.onButtonPressed(Button.AB, function () {
    variable_test = 0
})
input.onButtonPressed(Button.B, function () {
    variable_test += -1
})
let variable_test = 0
variable_test = 0
basic.forever(function () {
    basic.showNumber(variable_test,1)
})

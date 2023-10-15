myVariable = 0

def onevent_controller_1buttonUp_pressed_0():
    global myVariable
    drivetrain.drive(FORWARD)

def onevent_controller_1buttonDown_pressed_0():
    global myVariable
    drivetrain.drive(REVERSE)

def onevent_controller_1buttonRight_pressed_0():
    global myVariable
    drivetrain.turn(RIGHT)

def onevent_controller_1buttonLeft_pressed_0():
    global myVariable
    drivetrain.turn(LEFT)

def when_started1():
    global myVariable
    pass

# system event handlers
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
controller_1.buttonDown.pressed(onevent_controller_1buttonDown_pressed_0)
controller_1.buttonRight.pressed(onevent_controller_1buttonRight_pressed_0)
controller_1.buttonLeft.pressed(onevent_controller_1buttonLeft_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()


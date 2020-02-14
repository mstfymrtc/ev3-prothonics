#!/usr/bin/env python3
import prothonics
import numpy as np
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

color_sensor_front = ColorSensor(INPUT_3)
color_sensor_right = ColorSensor(INPUT_4)
color_sensor_left = ColorSensor(INPUT_1)
gyro_sensor = GyroSensor(INPUT_2)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_D)
sound = Sound()


# tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.4)
#steering_drive.on_for_rotations(-75, SpeedPercent(50), 1)
# tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 5)
# steering_drive.on_for_rotations(75, SpeedPercent(50), 1)
# tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 5)

# eat=just increase the score
# vrep robot sensor takılacak yer , hocaya sor
# robotun dönüş haraketlerini ayarla
# herbir kare boyutunu optimal olarak ayarla


# if frontColorSensor==yellow:
#    move_forward()
#    eat()
# elif rightColorSensor==yellow:
#    turn_right()
#    move_forward()
#    eat()
# elif leftColorSensor==yellow:
#    turn_left()
#    move_forward()
#    eat()
# elif frontColorSensor==white:
#    move_forward()
# elif rightColorSensor==white:
#    turn_right()
#    move_forward()
# elif leftColorSensor==white:
#    turn_left()
#    move_forward()
# else: #frontColorSensor==red and rightColorSensor==red and leftColorSensor==red
#    turn_backward()
# ------------------------------------------------------------------------------


def map_decision_to_action(decision):
    switcher = {
        "MoveForward": move_forward,
        "TurnBackward": turn_backward,
        "TurnRight": turn_right,
        "TurnLeft": turn_left,
        "Eat": eat,
    }
    func = switcher.get(decision, lambda: "Undefined decision")
    func()


def unknown_color():
    sound.speak('Unknown color!', espeak_opts='-a 200 -s 130 -v en+f1')


def move_forward():
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 0.9)
    print("I moved forward")
    tank_drive.off()


def turn_right():
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(-10), 0.55)
    tank_drive.on(SpeedPercent(10), SpeedPercent(-10))
    gyro_sensor.wait_until_angle_changed_by(87)
    print("I turned right")
    tank_drive.off()


def move_backward():
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(-10), 0.55)
    print("I moved backward")
    tank_drive.off()


def turn_left():
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(-10), 0.55)
    tank_drive.on(SpeedPercent(-10), SpeedPercent(10))
    gyro_sensor.wait_until_angle_changed_by(85)
    print("I turned left")
    tank_drive.off()


def turn_backward():
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(-10), 0.55)
    tank_drive.on(SpeedPercent(-10), SpeedPercent(10))
    gyro_sensor.wait_until_angle_changed_by(175)
    print("I turned backward")
    tank_drive.off()


def eat():
    print("eat")


colors = ["Unknown", "Black", "Blue", "Green",
          "Yellow", "Red", "White", "Brown"]
blindRobot = prothonics.Prothonics(1, 1)
blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

while True:
    sleep(1)

    front_sensor_value = color_sensor_front.color
    right_sensor_value = color_sensor_right.color
    left_sensor_value = color_sensor_left.color
    print("['{}', '{}', '{}'])".format(colors[front_sensor_value],
                                       colors[right_sensor_value],
                                       colors[left_sensor_value]))

    # check if any sensor detected incorrect value, if yes, dont run plan
    if front_sensor_value not in [4, 5, 6] or right_sensor_value not in [4, 5, 6] or left_sensor_value not in [4, 5, 6]:
        unknown_color()
        continue

    blindRobot.useBrain().reactTo(
        "perception(['{}', '{}', '{}'])".format(colors[front_sensor_value], colors[right_sensor_value], colors[left_sensor_value]),  "takeDecision()")

    print("Decisions:")
    decisions = blindRobot.useBrain().useMemory().getAllDecisions()[0][0]

    for decision in eval(decisions):
        map_decision_to_action(decision['D'])


# random.choice([4, 5,6])

# TODO: Eğer hiçbiri olmazsa, multi threading denenebilir:
# https://sites.google.com/site/ev3python/learn_ev3_python/threads

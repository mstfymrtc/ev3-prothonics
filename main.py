#!/usr/bin/env python3
import prothonics
import numpy as np
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

color_sensor_front = ColorSensor(INPUT_3)
color_sensor_right = ColorSensor(INPUT_4)
color_sensor_left = ColorSensor(INPUT_1)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

# tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.4)
steering_drive.on_for_rotations(-75, SpeedPercent(50), 1)
tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 5)
steering_drive.on_for_rotations(75, SpeedPercent(50), 1)
tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 5)

# steering_drive.on_for_rotations(55, SpeedPercent(50), 1)


colors = ["Unknown", "Black", "Blue", "Green", "Yellow", "Red", "White",
          "Brown"]
while True:
    print("front,right,left:", colors[color_sensor_front.color],
          colors[color_sensor_right.color], colors[color_sensor_left.color])
    sleep(1)

    # drive in a turn for 5 rotations of the outer motor
    # the first two parameters can be unit classes or percentages.

    # drive in a different turn for 3 seconds
    # tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)

    # robot ilerliyor
    # elif red_min < color_sensor.rgb < red_max:
    #     print("Red")
    #     check_sides(color_sensor.rgb)
    # if yellow_min < color_sensor.rgb < yellow_max:
    #     print("Yellow")
    # elif white_min < color_sensor.rgb < white_max:
    #     print("White")
    # else:
    #     print("Unknown")
    # print(color_sensor.rgb)
    # sleep(1)

#!/usr/bin/env python3
import prothonics
import numpy as np
import time
from pyvrep import VRep
from pyvrep.sensors import VisionSensor
import random
colors = {
    -29: "White",
    81: "Red",
    -102: "Yellow"
}

blindRobot = prothonics.Prothonics(1, 1)
blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")


class PioneerP3DX:

    def __init__(self, api: VRep):
        self._api = api
        self._left_motor = api.joint.with_position_control(
            "Pioneer_p3dx_leftMotor")
        self._right_motor = api.joint.with_position_control(
            "Pioneer_p3dx_rightMotor")
        self.robot=api.joint.with_position_control("Pioneer_p3dx")
        # self.set_two_motor(0.0,0.0)

        self._left_sensor = api.sensor.vision(
            "LeftRGBSensor")  # type: VisionSensor
        self._right_sensor = api.sensor.vision(
            "RightRGBSensor")  # type: VisionSensor
        self._front_sensor = api.sensor.vision(
            "FrontRGBSensor")  # type: VisionSensor

    def process_command(self, command, speed=2.0):
        switcher = {
            "MoveForward": self.move_forward,
            "MoveBackward": self.move_backward,
            "TurnRight": self.turn_right,
            "TurnLeft": self.turn_left,
            "Eat": self.eat,
        }
        func = switcher.get(command, lambda: "Undefined command")
        func(speed)

    def set_two_motor(self, left: float, right: float):
        self.robot.set_target_position(5)
        # self._right_motor.set_target_position(right)

    def turn_right(self, speed=2.0):

        self.set_two_motor(0.75, -0.75)
        print("turn_right")

    def turn_left(self, speed=2.0):
        self.set_two_motor(-0.75, 0.75)
        print("turn_left")

    def move_forward(self, speed=2.0):
        self.set_two_motor(1.4, 1.4)
        print("move forward")

    def move_backward(self, speed=2.0):
        self.set_two_motor(-1.6, 1.6)
        print("move_backward")

    def eat(self, speed):
        print("eaaaat")

    def reset_velocity(self):
        self.set_two_motor(0.0, 0.0)

    def right_color(self) -> int:
        image = self._right_sensor.raw_image(
            is_grey_scale=True)  # type: List[int]
        average = sum(image) / len(image)
        return average

    def left_color(self) -> int:
        image = self._left_sensor.raw_image(
            is_grey_scale=True)  # type: List[int]
        average = sum(image) / len(image)
        return average

    def front_color(self) -> int:
        image = self._front_sensor.raw_image(
            is_grey_scale=True)  # type: List[int]
        average = sum(image) / len(image)
        return average

    def plan(self, sensor_data):

        blindRobot.useBrain().reactTo(
            "perception(['{}', '{}', '{}'])".format(colors[sensor_data[0]], colors[sensor_data[1]], colors[sensor_data[2]]),  "takeDecision()")

        print("Decisions:")
        return blindRobot.useBrain().useMemory().getAllDecisions()[0][0]


def run():
    with VRep.connect("127.0.0.1", 19997) as api:
        robot = PioneerP3DX(api)
        # robot.reset_velocity()

        robot.move_forward()


run()
# blindRobot = prothonics.Prothonics(1, 1)
# blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

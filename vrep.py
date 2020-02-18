#!/usr/bin/env python3
import prothonics
import numpy as np
import time
from pyvrep import VRep
from pyvrep.sensors import VisionSensor
import random
colors = {
    -102: "Yellow",
    81: "Red",
    49: "Green"
}

blindRobot = prothonics.Prothonics(1, 1)
blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")


class PioneerP3DX:

    def __init__(self, api: VRep):
        self._api = api
        self._left_motor = api.joint.with_velocity_control(
            "Pioneer_p3dx_leftMotor")
        self._right_motor = api.joint.with_velocity_control(
            "Pioneer_p3dx_rightMotor")
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
            "TurnBackward": self.turn_backward,
            "RotateRight": self.rotate_right,
            "RotateLeft": self.rotate_left,
            "Eat": self.eat,
        }
        func = switcher.get(command, lambda: "Undefined command")
        func(speed)

    def set_two_motor(self, left: float, right: float):
        self._left_motor.set_target_velocity(left)
        self._right_motor.set_target_velocity(right)

    def rotate_right(self, speed=2.0):

        self.set_two_motor(0.7, -0.7)
        print("turn_right")

    def rotate_left(self, speed=2.0):
        self.set_two_motor(-0.75, 0.75)
        print("turn_left")

    def move_forward(self, speed=2.0):
        self.set_two_motor(1.4, 1.4)
        print("move forward")

    def turn_backward(self, speed=2.0):
        self.set_two_motor(-1.6, 1.6)
        print("move_backward")

    def eat(self, speed=2.0):
        print("eat")

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
        robot.reset_velocity()

        while True:
            # sense
            front_color = robot.front_color()
            right_color = robot.right_color()
            left_color = robot.left_color()
            # plan
            decisions = robot.plan([front_color, right_color, left_color])

            # act
            for decision in eval(decisions):

                robot.process_command(decision['D'])
                time.sleep(1)
                robot.reset_velocity()
            time.sleep(0.1)
run()

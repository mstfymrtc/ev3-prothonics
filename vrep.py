#!/usr/bin/env python3
import prothonics
import numpy as np
from time import sleep
from pyvrep import VRep
from pyvrep.sensors import VisionSensor

# color_sensor_front = ColorSensor(INPUT_3)
# color_sensor_right = ColorSensor(INPUT_4)
# color_sensor_left = ColorSensor(INPUT_1)


class PioneerP3DX:

    def __init__(self, api: VRep):
        self._api = api
        self._left_motor = api.joint.with_velocity_control(
            "Pioneer_p3dx_leftMotor")
        self._right_motor = api.joint.with_velocity_control(
            "Pioneer_p3dx_rightMotor")
        self._left_sensor = api.sensor.vision(
            "LeftColorSensor")  # type: VisionSensor
        self._right_sensor = api.sensor.vision(
            "RightColorSensor")  # type: VisionSensor
        self._front_sensor = api.sensor.vision(
            "FrontColorSensor")  # type: VisionSensor

    def set_two_motor(self, left: float, right: float):
        self._left_motor.set_target_velocity(left)
        self._right_motor.set_target_velocity(right)

    def rotate_right(self, speed=2.0):
        self.set_two_motor(speed, -speed)

    def rotate_left(self, speed=2.0):
        self.set_two_motor(-speed, speed)

    def move_forward(self, speed=2.0):
        self.set_two_motor(speed, speed)

    def move_backward(self, speed=2.0):
        self.set_two_motor(-speed, -speed)

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


colors = ["Unknown", "Black", "Blue", "Green",
          "Yellow", "Red", "White", "Brown"]
blindRobot = prothonics.Prothonics(1, 1)
blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

with VRep.connect("127.0.0.1", 19997) as api:
    robot = PioneerP3DX(api)
    # black color      :  43
    # white-gray color : -53
    while True:
        print(robot.left_color())
        robot.move_forward(1)
        # lclr = robot.left_color()
        # rclr = robot.right_color()
        # if lclr > 10:
        #     robot.rotate_left(0.3)
        # if rclr > 10:
        #     robot.rotate_right(0.3)
        # if lclr < -20 and rclr < -20:
        #     robot.move_forward(0.3)

        sleep(0.01)

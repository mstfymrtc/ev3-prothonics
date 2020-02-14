#!/usr/bin/env python3
# import prothonics
import numpy as np
import time
from pyvrep import VRep
from pyvrep.sensors import VisionSensor
import random
WHITE = 108.0
RED = 38.0
YELLOW = 70.0


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

    def set_two_motor(self, left: float, right: float):
        self._left_motor.set_target_velocity(left)
        self._right_motor.set_target_velocity(right)

    def rotate_right(self, speed=2.0):

        self.set_two_motor(speed, -speed)
        print("rotate_right")

    def rotate_left(self, speed=2.0):
        # t = time.process_time()
        self.set_two_motor(-speed, speed)
        print("rotate_left")
        # return time.process_time()-t

    def move_forward(self, speed=2.0):

        self.set_two_motor(speed, speed)
        print("move forward")

    def move_backward(self, speed=2.0):
        self.set_two_motor(-speed, -speed)
        print("move_backward")

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


colors = ["Unknown", "Black", "Blue", "Green",
          "Yellow", "Red", "White", "Brown"]
# blindRobot = prothonics.Prothonics(1, 1)
# blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

with VRep.connect("127.0.0.1", 19997) as api:
    robot = PioneerP3DX(api)
    # robot.reset_velocity()
    while True:
        left_color = robot.left_color()
        right_color = robot.right_color()
        front_color = robot.front_color()
    # robot.move_backward(5)

    # te = robot.rotate_left(3.1)
    # t = time.process_time()

    # time.sleep(2-((time.process_time()-t)+te))
    # robot.reset_velocity()
    # robot.move_forward(0)
    # robot.rotate_left(0)
    # sleep(1)
    # robot.move_forward(5)
    # robot.move_forward()
        if front_color == YELLOW:
            robot.move_forward()
        elif right_color == YELLOW:
            robot.rotate_right()
            robot.move_forward()
        elif left_color == YELLOW:
            robot.rotate_left()
            robot.move_forward()
        elif front_color == WHITE:
            robot.move_forward()
        elif right_color == WHITE:
            robot.rotate_right()
            robot.move_forward()
        elif left_color == WHITE:
            robot.rotate_left()
            robot.move_forward()
        else:
            robot.move_backward()
        time.sleep(0.1)

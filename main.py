#!/usr/bin/env python3
import prothonics
import numpy as np
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
color_sensor_front = ColorSensor(INPUT_3)
color_sensor_right = ColorSensor(INPUT_4)
color_sensor_left = ColorSensor(INPUT_1)
gyro_sensor = GyroSensor(INPUT_2)


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)


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
        "Eat": eat
    }
    func = switcher.get(decision, lambda: "Undefined decision")
    func()

#TODO: Her hareket fonksiyonu sonunda sleep edilebilir.
def move_forward():
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 0.9)
    print("move forward")

    # TODO:!!!!!!!!!!!!ÖRN MOVE FORWARD ÇALIŞINCA, PRINT DİREKT Mİ YAZIYOR YOKSA
    # BİRAZ DELAYDEN SONRA, YANİ MOTOR HAREKETİ BİTİNCE Mİ ÇALIŞIYOR?
    # HEMEN ÇALIŞIYORSA, BU DEMEK OLUYORKİ ROBOTUN HAREKETLERİ BİTMEDEN SONRAKİ
    # SATIRLAR ÇALIŞIYOR, ONDAN ÖTÜRÜ SENSÖR DEĞERLERİ YANLIŞ GELİYOR!
    # eğer öyle ise : check wait while of motor classes:
    # https://sites.google.com/site/ev3python/learn_ev3_python/basics


def turn_right():
    move_backward()
    tank_drive.on(SpeedPercent(10), SpeedPercent(-10))
    gyro_sensor.wait_until_angle_changed_by(80)
    print("turn right")


def move_backward():
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(-10), 0.55)
    print("move backward")


def turn_left():
    move_backward()
    tank_drive.on(SpeedPercent(-10), SpeedPercent(10))
    gyro_sensor.wait_until_angle_changed_by(80)
    print("turn left")

    # steering_drive.on_for_rotations(-65, SpeedPercent(10), 0.9)


def turn_backward():
    print("turn backward")


def eat():
    print("eat")


colors = ["Unknown", "Black", "Blue", "Green",
          "Yellow", "Red", "White", "Brown"]
blindRobot = prothonics.Prothonics(1, 1)
blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")


while True:
    #sleep(6) #TODO:belki while başında bekletilebilir?
    front_sensor_value = color_sensor_front.color
    right_sensor_value = color_sensor_right.color
    left_sensor_value = color_sensor_left.color

    # sleep(7) #TODO:değer geldikten sonra biraz bekletilebilir belki:?

    print("['{}', '{}', '{}'])".format(colors[front_sensor_value],
                                       colors[right_sensor_value],
                                       colors[left_sensor_value]))

    blindRobot.useBrain().reactTo(
        "perception(['{}', '{}', '{}'])".format(colors[front_sensor_value], colors[right_sensor_value], colors[left_sensor_value]),  "takeDecision()")

    print("Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    decisions = blindRobot.useBrain().useMemory().getAllDecisions()[0][0]

    for decision in eval(decisions):
        map_decision_to_action(decision['D'])

    # sleep(1) =>bunu genelde her while loopu
    # sonuna koyurlar, belki denenebilir.

    # sleep(6) #TODO:belki while sonunda bekletilebilir, hem bu sırada tüm movementlar biter?



# random.choice([4, 5,6])

#TODO: Eğer hiçbiri olmazsa, multi threading denenebilir:
#https://sites.google.com/site/ev3python/learn_ev3_python/threads


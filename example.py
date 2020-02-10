import prothonics
import numpy as np
#eat=just increase the score

#if frontColorSensor==white:
    #move_forward()
#elif frontColorSensor==yellow:
    #move_forward()
    #eat()
#else: öne gidemez
    #if RightColorSensor==white:
        #turn_right()
        #move_forward()
    #elif RightColorSensor==yellow:
        #turn_right()
        #move_forward()
        #eat()
    #else: öne ve sağa gidemez
        #if LeftColorSensor==white:
            #turn_left()
            #move_forward()
        #elif LeftColorSensor==yellow:
            #turn_left()
            #move_forward()
            #eat()
        #else: öne,sağa ve sola gidemez



def map_decision_to_action(decision):
    switcher = {
        "MoveForward": move_forward,
        "MoveBackward": move_backward,
        "TurnRight": turn_right,
        "TurnLeft": turn_left,
        "Eat": eat
    }
    func=switcher.get(decision, lambda: "Undefined decision")
    func()


def move_forward():
    print("move forward")
    #tank fonk. çalıştırılacak

def turn_right():
    print("turn right")

def turn_left():
    print("turn left")

def move_backward():
    print("move backward")

def eat():
    print("eat")


color_sensor_front = 4 #ColorSensor(INPUT_3)
color_sensor_right = 5
color_sensor_left = 6

colors = ["Unknown", "Black", "Blue", "Green", "Yellow", "Red", "White",
          "Brown"]

def main():

    blindRobot = prothonics.Prothonics(1, 1)
    blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

    #fstring -> string içerisinde variable çağırabilme
    blindRobot.useBrain().reactTo(f"perception(['{colors[color_sensor_front]}', '{colors[color_sensor_right]}', '{colors[color_sensor_left]}'])",  "takeDecision()")
    print("Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    a = blindRobot.useBrain().useMemory().getAllDecisions()[0][0]

    for i in eval(a):
        map_decision_to_action(i['D'])



if __name__ == '__main__':
    main()

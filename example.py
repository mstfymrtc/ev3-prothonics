# coding : utf-8

'''
Copyright 2019-2020 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

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

            


def main():

    blindRobot = prothonics.Prothonics(10, 10)
    blindRobot.useBrain().useLearning().learnKnowledgeBaseFromFile("behaviour.pl")

    blindRobot.useBrain().reactTo("perception(['White', 'Red', 'Red'])",  "takeDecision()")
    print("West obstacle: Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    print(blindRobot.useBrain().useMemory().getAllDecisions())



if __name__ == '__main__':
    main()

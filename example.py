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

def main():

    blindRobot = prothonics.Prothonics(10, 10)
    blindRobot.useBrain().useLearning().learnKnoledgeBaseFromFile("behaviour.pl")

    blindRobot.useBrain().reactTo("perception(['False', 'True', 'False', 'False'])",  "takeDecision()")
    print("West obstacle: Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    print(blindRobot.useBrain().useMemory().getAllDecisions())

    blindRobot.useBrain().reactTo("perception(['True', 'False', 'False', 'False'])",  "takeDecision()")
    print("North obstacle: Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    print(blindRobot.useBrain().useMemory().getAllDecisions())

    blindRobot.useBrain().reactTo("perception(['True', 'True', 'True', 'False'])",  "takeDecision()")
    print("North, West and East obstacle: Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    print(blindRobot.useBrain().useMemory().getAllDecisions())

    blindRobot.useBrain().reactTo("perception(['True', 'False', 'False', 'False'])", "takeDecision()")
    print("North obstacle: Facts and Decisions:")
    print(blindRobot.useBrain().useMemory().getAllFacts())
    print(blindRobot.useBrain().useMemory().getAllDecisions())


if __name__ == '__main__':
    main()

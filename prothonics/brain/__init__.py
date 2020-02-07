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


from pyswip import Prolog
import prothonics.brain.learning
import prothonics.brain.memory
import prothonics.brain.behaviour

class Brain:
    '''
        The main intelligent controller of the Prothonics Agent.
    '''
    __learning = None
    __memory = None
    __behaviour = None
    __prologEngine = None  # Prolog engine, reasoning and learning core

    def __init__(self,  decisionsLen, factsLen):
        self.__prologEngine = Prolog()  # The engine given by Pyswip SWI Prolog library
        self.__learning = learning.Learning(self.__prologEngine)
        self.__memory = memory.Memory(decisionsLen, factsLen)
        self.__behaviour = behaviour.Behaviour(self.__prologEngine)

    def useLearning(self):
        return self.__learning

    def useMemory(self):
        return self.__memory

    def useBehaviour(self):
        return self.__behaviour

    def reactTo(self, fact, decisionFactClass):
        '''
        Learns a new fact and take a decision about it. It stores in memory the new fact and the new decision.
        :param fact: the new fact to learn, it's a string.
        :param decisionFactClass: the class of the fact that describes the solution.
        :return:
        '''
        fact = str(fact)
        decisionFactClass = str(decisionFactClass)
        self.__learning.learnNewFact(fact)
        self.__memory.putNewFact(fact)
        newDecision = self.__behaviour.takeDecision(decisionFactClass=decisionFactClass, singleOut=True)
        if newDecision:
            self.__memory.putNewDecision(newDecision)
        return

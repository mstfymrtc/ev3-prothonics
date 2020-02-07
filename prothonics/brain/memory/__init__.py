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

from collections import deque
import numpy as np
import time

class Memory:
    '''
        Prothonics Agent Brain module for data retrieving.
    '''
    __decisions = None  # Array containing taken decisions (FIFO)
    __facts = None  # Array containing known facts (FIFO)

    def __init__(self, decisionsLen, factsLen):
        decisionsLen = int(decisionsLen)
        factsLen = int(factsLen)
        self.__decisions = list(np.zeros(decisionsLen))
        self.__facts = list(np.zeros(factsLen))

    def getLastNArrayElements(self, arr, num):
        num = int(num)
        if len(arr) >= num:
            return arr[len(self.__decisions) - num:]

    def putTimestampedElementToArray(self, arr, elem):
        arr = list(arr)
        arr.append([elem, time.time()])
        arr = deque(arr)
        arr.popleft()
        return list(arr)

    def getAllDecisions(self):
        return self.__decisions

    def getAllFacts(self):
        return self.__facts

    def getLastNDecisions(self, num):
        return self.getLastNArrayElements(self.__decisions, num)

    def getLastNFacts(self, num):
        return self.getLastNArrayElements(self.__facts, num)

    def putNewDecision(self, decision):
        decision = str(decision)
        self.__decisions = self.putTimestampedElementToArray(self.__decisions, decision)
        return

    def putNewFact(self, fact):
        fact = str(fact)
        self.__facts = self.putTimestampedElementToArray(self.__facts, fact)
        return

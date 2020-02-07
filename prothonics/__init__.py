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


import prothonics.brain


class Prothonics:
    '''
        Agent is a proactive element provided with Sense, Brain and Act modules.
    '''
    __sense = None
    __brain = None
    __act = None

    def __init__(self,  decisionsLen, factsLen):
        # self.__sense =  #TODO
        # self.__act =  #TODO
        self.__brain = brain.Brain( decisionsLen, factsLen)

    def useBrain(self):
        return self.__brain

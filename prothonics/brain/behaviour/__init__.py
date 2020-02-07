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


class Behaviour:
    '''
        The behavioural module of a Prothonics Agent Brain.
    '''
    __prologEngine = None  # Prolog Engine, reasoning and learning core

    def __init__(self, prologEngine):
        self.__prologEngine = prologEngine

    def takeDecision(self, decisionFactClass, singleOut=True):
        '''
        Given the facts already known, it takes a new decision.
        :return: decision, a string.
        '''
        decisionFactClass = str(decisionFactClass).replace('"', "'")
        decisionFact = decisionFactClass.split('(')[0] + '(D)'
        try:
            out = list(self.__prologEngine.query(decisionFact))
        except:  # If Prolog doesn't work (maybe because it can't receive data from sensors), do nothing
            out = []
        if len(out) > 0:  # If we can take more than one decision, we take the 1st one
            if singleOut:
                decision = out[0]['D']
            else:
                decision = out
        else:
            decision = None
        return decision

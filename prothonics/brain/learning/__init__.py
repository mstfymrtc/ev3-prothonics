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


class Learning:
    '''
        The learning module of a Prothinics Agent Brain.
    '''
    __prologEngine = None  # Prolog Engine, reasoning and learning core

    def __init__(self, prologEngine):
        self.__prologEngine = prologEngine

    def cleanIdeas(self, aboutFact):
        '''
        Deletes old facts from Prolog Engine.
        :param aboutFact: fact class that has to be cleaned.
        :return:
        '''
        aboutFact = str(aboutFact)
        factClass = aboutFact.split('(')[0] + '(_)'
        self.__prologEngine.retractall(factClass)
        return

    def learnKnoledgeBaseFromFile(self, prologFilePath):
        '''
        Learns from a SWI Prolog file.
        :param prologFilePath: The path of the Prolog (.pl or .txt) file we need to use.
        :return:
        '''
        assert isinstance(prologFilePath, str)
        self.__prologEngine.consult(prologFilePath)
        return

    def learnNewFact(self, fact):
        '''
        Asserts a new fact.
        :param fact: a string containing a Prolog fact.
        :return:
        '''
        fact = str(fact).replace('"', "'")
        self.cleanIdeas(fact)
        self.__prologEngine.assertz(fact)
        return

"""
Personal AI System
User Memory Manager v0.5

Advanced user information storage
"""

from memory.memory_engine import MemoryEngine



class UserMemory:


    def __init__(self):

        self.memory = MemoryEngine()



    def save_user_fact(self, fact):

        return self.memory.remember(
            fact,
            "user_information"
        )



    def search_user_information(self, keyword=None):

        results = self.memory.recall(
            keyword
        )

        filtered = []

        for item in results:

            if item[1] == "user_information":

                filtered.append(item[0])


        return filtered



    def remember_sentence(self, sentence):

        keywords = [

            "من هستم",
            "اسم من",
            "منم",
            "من",
            "به یاد بسپار",
            "یادآوری کن"

        ]


        for key in keywords:

            if key in sentence:

                self.save_user_fact(
                    sentence
                )

                return True


        return False



    def get_profile(self):

        return self.search_user_information()

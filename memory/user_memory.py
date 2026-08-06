"""
Personal AI System
Smart User Memory v0.6
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



    def remember_sentence(self, sentence):


        text = sentence.strip()



        # جمله های سوالی ذخیره نشوند

        blocked = [

            "؟",
            "چی",
            "کی",
            "چرا",
            "چگونه",
            "چطور"

        ]


        for word in blocked:

            if word in text:

                return False




        patterns = [

            "اسم من",
            "من هستم",
            "من سازنده",
            "من دارم",
            "به یاد بسپار",
            "یادآوری کن"

        ]



        for pattern in patterns:


            if pattern in text:


                self.save_user_fact(
                    text
                )

                return True



        return False





    def search_user_information(self):


        results = self.memory.recall()



        facts = []


        for item in results:


            if item[1] == "user_information":

                facts.append(
                    item[0]
                )


        return facts




    def get_profile(self):

        return self.search_user_information()

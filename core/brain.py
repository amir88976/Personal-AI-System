"""
Personal AI System
Brain Engine v1.1

Profile Memory Integrated
"""


from core.identity import IdentityEngine
from core.dialogue_manager import DialogueManager
from core.personality import PersonalityEngine


from memory.profile_memory import ProfileMemory



class BrainEngine:


    def __init__(self):

        self.identity = IdentityEngine()

        self.dialogue = DialogueManager()

        self.personality = PersonalityEngine()

        self.profile = ProfileMemory()



    def process(self, message):


        message = str(message).strip()



        # یادگیری اطلاعات کاربر

        learned = self.profile.learn(
            message
        )


        if learned:

            return self.personality.format(
                learned
            )



        # پرسش درباره خودش

        if (
            "من کی هستم" in message
            or "چی درباره من میدونی" in message
        ):


            info = self.profile.get_information()



            if info:

                return self.personality.format(

                    "چیزهایی که می‌دانم:\n"
                    +
                    "\n".join(info)

                )


            return self.personality.format(
                "هنوز اطلاعات زیادی درباره تو ندارم."
            )



        # هویت AI

        answer = self.identity.check(
            message
        )


        if answer:

            return self.personality.format(
                answer
            )



        # مکالمه

        answer = self.dialogue.reply(
            message
        )


        if answer:

            return self.personality.format(
                answer
            )



        return self.personality.format(
            "جالبه 😊 ادامه بده، گوش می‌کنم."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

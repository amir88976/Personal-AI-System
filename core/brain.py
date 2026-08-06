"""
Personal AI System
Brain Engine v1.0
"""


from core.identity import IdentityEngine
from core.dialogue_manager import DialogueManager
from core.personality import PersonalityEngine



class BrainEngine:


    def __init__(self):

        self.identity = IdentityEngine()

        self.dialogue = DialogueManager()

        self.personality = PersonalityEngine()



    def process(self, message):


        message = str(message).strip()



        # اول هویت

        answer = self.identity.check(
            message
        )


        if answer:

            return self.personality.format(
                answer
            )



        # بعد مکالمه

        answer = self.dialogue.reply(
            message
        )


        if answer:

            return self.personality.format(
                answer
            )



        # جواب پیش فرض بهتر

        return self.personality.format(
            "جالبه 😊 بیشتر برام توضیح بده."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

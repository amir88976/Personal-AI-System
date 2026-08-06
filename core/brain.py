"""
Personal AI System
Brain Engine v1.4

Emotion + Identity + Memory
"""


from core.identity import IdentityEngine
from core.dialogue_manager import DialogueManager
from core.personality import PersonalityEngine
from core.emotion_engine import EmotionEngine


from memory.profile_memory import ProfileMemory




class BrainEngine:


    def __init__(self):

        self.identity = IdentityEngine()

        self.dialogue = DialogueManager()

        self.personality = PersonalityEngine()

        self.emotion = EmotionEngine()

        self.profile = ProfileMemory()




    def process(self, message):


        message = str(message).strip()



        # اول یادگیری اطلاعات کاربر

        learned = self.profile.learn(
            message
        )


        if learned:

            return self.personality.format(
                learned
            )



        # بررسی احساس و حالت کاربر

        emotion = self.emotion.analyze(
            message
        )


        emotion_reply = self.emotion.response(
            emotion
        )


        if emotion_reply:

            return self.personality.format(
                emotion_reply
            )



        # بررسی هویت

        identity_answer = self.identity.check(
            message
        )


        if identity_answer:

            return self.personality.format(
                identity_answer
            )



        # مکالمه معمولی

        dialogue_answer = self.dialogue.reply(
            message
        )


        if dialogue_answer:

            return self.personality.format(
                dialogue_answer
            )



        return self.personality.format(
            "دارم گوش می‌کنم 😊 بیشتر توضیح بده."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

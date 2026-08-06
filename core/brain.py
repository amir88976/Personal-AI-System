"""
Personal AI System
Brain Engine v0.9

Identity + Context integrated core
"""


from core.decision import DecisionEngine
from core.personality import PersonalityEngine


try:
    from core.identity import IdentityEngine
except Exception:
    IdentityEngine = None


try:
    from core.dialogue_manager import DialogueManager
except Exception:
    DialogueManager = None


try:
    from memory.conversation_memory import ConversationMemory
except Exception:
    ConversationMemory = None



class BrainEngine:


    def __init__(self):

        self.name = "Personal AI"


        self.decision = DecisionEngine()


        self.personality = PersonalityEngine()


        self.identity = None


        if IdentityEngine:

            try:
                self.identity = IdentityEngine()

            except Exception:
                pass



        self.dialogue = None


        if DialogueManager:

            try:
                self.dialogue = DialogueManager()

            except Exception:
                pass



        self.context = None


        if ConversationMemory:

            try:
                self.context = ConversationMemory()

            except Exception:
                pass




    def process(self, message):


        message = str(message).strip()



        if self.context:

            self.context.add_message(
                "user",
                message
            )



        # اول هویت را بررسی کن

        if self.identity:


            identity_answer = self.identity.check(
                message
            )


            if identity_answer:


                if self.context:

                    self.context.add_message(
                        "ai",
                        identity_answer
                    )


                return self.personality.format(
                    identity_answer
                )



        # بعد مکالمه عادی

        if self.dialogue:


            reply = self.dialogue.reply(
                message
            )


            if reply:

                if self.context:

                    self.context.add_message(
                        "ai",
                        reply
                    )


                return self.personality.format(
                    reply
                )



        return self.personality.format(
            "گوش کردم 👌 ادامه بده، دارم دنبال می‌کنم."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

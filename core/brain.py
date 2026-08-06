"""
Personal AI System
Brain Engine v0.7

Dialogue integrated core
"""


from core.decision import DecisionEngine
from core.personality import PersonalityEngine


try:
    from core.dialogue_manager import DialogueManager
except Exception:
    DialogueManager = None


try:
    from memory.memory_engine import MemoryEngine
except Exception:
    MemoryEngine = None



class BrainEngine:


    def __init__(self):

        self.name = "Personal AI"


        self.decision = DecisionEngine()


        self.personality = PersonalityEngine()


        self.dialogue = None


        if DialogueManager:

            try:
                self.dialogue = DialogueManager()

            except Exception:
                pass



        self.memory = None


        if MemoryEngine:

            try:
                self.memory = MemoryEngine()

            except Exception:
                pass




    def process(self, message):


        message = str(message).strip()



        if not message:

            return "پیامی دریافت نکردم."



        # اول مکالمه طبیعی

        if self.dialogue:


            reply = self.dialogue.reply(
                message
            )


            if reply:

                return self.personality.format(
                    reply
                )



        # ذخیره گفتگو

        if self.memory:

            try:

                self.memory.remember(
                    message,
                    "conversation"
                )

            except Exception:

                pass



        analysis = self.decision.analyze(
            message
        )



        return self.personality.format(

            self.generate_answer(
                message,
                analysis
            )

        )





    def generate_answer(
            self,
            message,
            analysis
    ):


        if analysis["type"] == "question":

            return (
                "سؤالت رو گرفتم 😊 "
                "دارم بررسی می‌کنم."
            )


        return (
            "گوش کردم 👌 "
            "بیشتر برام توضیح بده."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

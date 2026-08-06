"""
Personal AI System
Brain Engine v0.6

Conversation integrated core
"""


from core.decision import DecisionEngine
from core.personality import PersonalityEngine


try:
    from core.conversation import ConversationEngine
except Exception:
    ConversationEngine = None



try:
    from memory.memory_engine import MemoryEngine
except Exception:
    MemoryEngine = None



class BrainEngine:


    def __init__(self):

        self.name = "Personal AI"


        self.decision = DecisionEngine()


        self.personality = PersonalityEngine()


        self.conversation = None


        if ConversationEngine:

            try:

                self.conversation = ConversationEngine()

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



        # اول مکالمه طبیعی را بررسی کن

        if self.conversation:


            answer = self.conversation.process(
                message
            )


            if answer:

                return self.personality.format(
                    answer
                )



        # ذخیره در حافظه گفتگو

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
                "سؤال جالبی پرسیدی. "
                "در حال تحلیل آن هستم."
            )



        return (
            "پیامت دریافت شد و توسط هسته "
            "Personal AI پردازش شد."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

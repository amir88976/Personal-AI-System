"""
Personal AI System
Brain Engine v0.8

Context memory integrated core
"""


from core.decision import DecisionEngine
from core.personality import PersonalityEngine


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



        if not message:

            return "پیامی دریافت نکردم."



        # ذخیره پیام کاربر

        if self.context:

            self.context.add_message(
                "user",
                message
            )



        # مکالمه طبیعی

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



        analysis = self.decision.analyze(
            message
        )



        answer = self.generate_answer(
            message,
            analysis
        )



        if self.context:

            self.context.add_message(
                "ai",
                answer
            )



        return self.personality.format(
            answer
        )





    def generate_answer(
            self,
            message,
            analysis
    ):


        recent = ""


        if self.context:

            history = self.context.get_recent(3)

            recent = str(history)



        if analysis["type"] == "question":

            return (
                "سؤال تو دریافت شد 😊 "
                "آخرین گفتگوهای ما را هم در نظر می‌گیرم."
            )



        return (
            "گوش کردم 👌 "
            "ادامه بده، دارم دنبال می‌کنم."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

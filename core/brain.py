"""
Personal AI System
Brain Engine v0.4

Integrated reasoning core
"""


from datetime import datetime


from core.decision import DecisionEngine
from core.personality import PersonalityEngine


try:
    from memory.memory_engine import MemoryEngine
except Exception:
    MemoryEngine = None



class BrainEngine:


    def __init__(self):

        self.name = "Personal AI"


        self.decision = DecisionEngine()


        self.personality = PersonalityEngine()


        self.memory = None


        if MemoryEngine:

            try:
                self.memory = MemoryEngine()

            except Exception:
                pass



    def process(self, message):


        message = str(message).strip()


        if not message:

            return "پیام خالی است."



        analysis = self.decision.analyze(
            message
        )



        if self.memory:

            try:

                self.memory.remember(
                    message,
                    analysis["type"]
                )

            except Exception:

                pass



        answer = self.generate_answer(
            message,
            analysis
        )



        return self.personality.format(
            answer
        )





    def generate_answer(
            self,
            message,
            analysis
    ):


        category = analysis["type"]



        if category == "question":

            return (
                "سؤال تو دریافت شد. "
                "در نسخه‌های بعدی موتور تحلیل "
                "پاسخ‌دهی پیشرفته اضافه می‌شود."
            )



        elif category == "memory":

            return (
                "درخواست حافظه ثبت شد."
            )



        elif category == "planning":

            return (
                "درخواست برنامه‌ریزی شناسایی شد."
            )



        return (
            "پیام تو دریافت شد و توسط هسته "
            "Personal AI پردازش شد."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

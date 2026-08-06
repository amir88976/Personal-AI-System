"""
Personal AI System
Brain Engine v0.5

Memory integrated core
"""


from core.decision import DecisionEngine
from core.personality import PersonalityEngine


try:
    from memory.memory_engine import MemoryEngine
except Exception:
    MemoryEngine = None


try:
    from memory.user_memory import UserMemory
except Exception:
    UserMemory = None




class BrainEngine:


    def __init__(self):

        self.name = "Personal AI"


        self.decision = DecisionEngine()


        self.personality = PersonalityEngine()


        self.memory = None

        self.user_memory = None



        if MemoryEngine:

            try:
                self.memory = MemoryEngine()

            except Exception:
                pass



        if UserMemory:

            try:
                self.user_memory = UserMemory()

            except Exception:
                pass




    def process(self, message):


        message = str(message).strip()



        if not message:

            return "پیام خالی است."



        analysis = self.decision.analyze(
            message
        )



        # ذخیره گفتگو

        if self.memory:

            try:

                self.memory.remember(
                    message,
                    analysis["type"]
                )

            except Exception:
                pass




        # بررسی اطلاعات شخصی

        if self.user_memory:


            try:

                saved = self.user_memory.remember_sentence(
                    message
                )


            except Exception:

                saved = False




        # درخواست مشاهده حافظه

        if "من کی هستم" in message or "چی درباره من میدونی" in message:


            if self.user_memory:

                profile = self.user_memory.get_profile()


                if profile:

                    return self.personality.format(
                        "اطلاعاتی که ذخیره کردم:\n"
                        +
                        "\n".join(profile)
                    )



                return self.personality.format(
                    "هنوز اطلاعاتی از تو ذخیره نکردم."
                )



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


        if analysis["type"] == "memory":

            return (
                "اطلاعاتت را برای حافظه ثبت کردم."
            )


        if analysis["type"] == "question":

            return (
                "سؤال دریافت شد. "
                "موتور تحلیل من در حال ارتقا است."
            )


        return (
            "پیام دریافت شد و در هسته Personal AI پردازش شد."
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

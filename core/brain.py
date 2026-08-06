"""
Personal AI System
Core Brain Engine v0.3

Main reasoning layer
"""

from datetime import datetime

try:
    from memory.memory_engine import MemoryEngine
except Exception:
    MemoryEngine = None


try:
    from core.personality import PersonalityEngine
except Exception:
    PersonalityEngine = None



class BrainEngine:

    def __init__(self):

        self.name = "Personal AI"

        self.memory = None
        self.personality = None


        if MemoryEngine:

            try:
                self.memory = MemoryEngine()

            except Exception:
                self.memory = None



        if PersonalityEngine:

            try:
                self.personality = PersonalityEngine()

            except Exception:
                self.personality = None



    def think(self, message):

        message = str(message).strip()


        if not message:

            return "پیامی دریافت نکردم."



        # ذخیره گفتگو در حافظه

        if self.memory:

            try:

                self.memory.remember(
                    message,
                    "conversation"
                )

            except Exception:
                pass



        response = self.generate_response(message)


        return response



    def generate_response(self, message):


        text = message.lower()



        if "سلام" in message or "hello" in text:

            answer = (
                "سلام 👋\n"
                "من Personal AI هستم. "
                "هسته جدید من فعال شده."
            )



        elif "اسم" in message:

            answer = (
                f"نام من {self.name} است."
            )



        elif "حافظه" in message:

            if self.memory:

                memories = self.memory.get_recent(5)

                answer = (
                    "آخرین اطلاعات ذخیره شده:\n"
                    +
                    "\n".join(
                        [
                            str(x[0])
                            for x in memories
                        ]
                    )
                )

            else:

                answer = "حافظه هنوز فعال نشده."



        else:

            answer = (
                "پیام تو دریافت شد.\n"
                "من در حال پردازش و یادگیری ساختار جدید هستم."
            )



        if self.personality:

            try:

                answer = self.personality.format(
                    answer
                )

            except Exception:
                pass



        return answer





brain = BrainEngine()



def process_brain(message):

    return brain.think(message)

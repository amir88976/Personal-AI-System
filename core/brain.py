"""
Personal AI System
Brain Engine v2.6

Persistent Conversation Memory
"""


from core.llm_engine import LLMEngine
from core.prompt_builder import PromptBuilder
from core.personality import PersonalityEngine


from memory.profile_memory import ProfileMemory
from memory.chat_database import ChatDatabase




class BrainEngine:


    def __init__(self):

        self.llm = LLMEngine()

        self.prompt = PromptBuilder()

        self.personality = PersonalityEngine()

        self.memory = ProfileMemory()

        self.chat_db = ChatDatabase()




    def process(
        self,
        message
    ):


        message = str(message).strip()



        # ذخیره پیام کاربر

        self.chat_db.save(
            "user",
            message
        )



        # گرفتن اطلاعات کاربر

        user_memory = (
            self.memory.get_information()
        )



        # گرفتن تاریخچه قبلی

        history = (
            self.chat_db.load(20)
        )



        # ساخت پرامپت کامل

        final_prompt = self.prompt.build(

            message,

            user_memory,

            history

        )



        # تولید پاسخ

        answer = self.llm.generate(

            final_prompt

        )



        # ذخیره جواب AI

        self.chat_db.save(

            "ai",

            answer

        )



        return self.personality.format(

            answer

        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

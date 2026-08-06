"""
Personal AI System
Brain Engine v2.0

LLM First Architecture
"""


from core.llm_engine import LLMEngine
from core.personality import PersonalityEngine

from memory.profile_memory import ProfileMemory



class BrainEngine:


    def __init__(self):

        self.llm = LLMEngine()

        self.personality = PersonalityEngine()

        self.memory = ProfileMemory()



    def process(self, message):


        message = str(message).strip()



        # گرفتن اطلاعات ذخیره شده

        user_memory = self.memory.get_information()



        # ساخت زمینه برای هوش مصنوعی

        context = {

            "user_memory": user_memory,

            "message": message

        }



        # تولید پاسخ

        answer = self.llm.generate(
            context
        )



        return self.personality.format(
            answer
        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

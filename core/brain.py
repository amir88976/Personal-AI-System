"""
Personal AI System
Brain Engine v2.3
"""


from core.llm_engine import LLMEngine
from core.prompt_builder import PromptBuilder
from core.personality import PersonalityEngine


from memory.profile_memory import ProfileMemory



class BrainEngine:


    def __init__(self):

        self.llm = LLMEngine()

        self.prompt = PromptBuilder()

        self.personality = PersonalityEngine()

        self.memory = ProfileMemory()



    def process(
        self,
        message
    ):


        message = str(message).strip()



        user_memory = (
            self.memory.get_information()
        )



        final_prompt = self.prompt.build(

            message,

            user_memory

        )



        answer = self.llm.generate(

            final_prompt

        )



        return self.personality.format(

            answer

        )





brain = BrainEngine()



def process_brain(message):

    return brain.process(message)

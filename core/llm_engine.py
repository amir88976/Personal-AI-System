"""
Personal AI System
LLM Engine v2.3
"""


from core.ai_provider import AIProvider
from core.local_ai_engine import LocalAIEngine



class LLMEngine:


    def __init__(self):

        self.provider = AIProvider()

        self.local = LocalAIEngine()


        self.provider.set_provider(
            "local",
            self.local
        )



    def generate(
        self,
        prompt
    ):


        return self.provider.generate(
            prompt
        )

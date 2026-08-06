"""
Personal AI System
LLM Engine v3.1
"""


from core.llm_gateway import LLMGateway
from core.local_ai_engine import LocalAIEngine




class LLMEngine:


    def __init__(self):

        self.gateway = LLMGateway()

        self.local = LocalAIEngine()


        self.gateway.connect(
            self.local
        )




    def generate(
        self,
        prompt
    ):


        return self.gateway.ask(
            prompt
        )

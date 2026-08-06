"""
Personal AI System
AI Configuration v3.2
"""


class AIConfig:


    def __init__(self):

        self.settings = {

            "model_name": "Personal-LLM",

            "temperature": 0.7,

            "max_tokens": 512,

            "memory_enabled": True,

            "personality": "friendly"

        }




    def get(
        self,
        key
    ):

        return self.settings.get(
            key
        )




    def set(
        self,
        key,
        value
    ):

        self.settings[key] = value




    def all(self):

        return self.settings

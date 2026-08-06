"""
Personal AI System
Local AI Engine v3.3
"""


from core.model_interface import BaseModel




class LocalAIEngine(BaseModel):


    def __init__(self):

        self.name = "Local Model"




    def generate(
        self,
        prompt,
        config=None
    ):


        return (
            "مدل محلی آماده اتصال است. "
            "پیام دریافت شد."
        )

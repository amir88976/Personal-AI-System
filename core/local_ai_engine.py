"""
Personal AI System
Local AI Engine v2.9
"""


from core.model_adapter import ModelAdapter




class LocalAIEngine:


    def __init__(self):

        self.adapter = ModelAdapter()



    def generate(
        self,
        prompt
    ):


        response = self.adapter.generate(
            prompt
        )


        if response:

            return response



        return (
            "مدل زبانی هنوز متصل نشده است."
        )

"""
Personal AI System
Local AI Engine v3.4
"""


from core.model_interface import BaseModel
from core.model_connector import ModelConnector




class LocalAIEngine(BaseModel):


    def __init__(self):

        self.connector = ModelConnector()



    def attach_model(
        self,
        model
    ):

        self.connector.connect(
            model
        )



    def generate(
        self,
        prompt,
        config=None
    ):


        return self.connector.generate(
            prompt,
            config
        )

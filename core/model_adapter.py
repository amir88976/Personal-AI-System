"""
Personal AI System
Model Adapter v2.9
"""


class ModelAdapter:


    def __init__(self):

        self.model = None

        self.connected = False



    def connect(
        self,
        model
    ):

        self.model = model

        self.connected = True




    def generate(
        self,
        prompt
    ):


        if not self.connected:

            return None



        return self.model.generate(
            prompt
        )

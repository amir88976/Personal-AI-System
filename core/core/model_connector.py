"""
Personal AI System
Model Connector v3.4
"""


class ModelConnector:


    def __init__(self):

        self.client = None

        self.connected = False



    def connect(
        self,
        client
    ):

        self.client = client

        self.connected = True




    def generate(
        self,
        prompt,
        config=None
    ):


        if not self.connected:

            return (
                "مدل واقعی هنوز وصل نشده است."
            )



        return self.client.generate(
            prompt,
            config
        )

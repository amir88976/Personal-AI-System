"""
Personal AI System
Local AI Engine v3.5
"""


from core.model_server_bridge import ModelServerBridge



class LocalAIEngine:


    def __init__(self):

        self.bridge = ModelServerBridge()



    def connect_server(
        self,
        url
    ):

        self.bridge.connect(
            url
        )



    def generate(
        self,
        prompt,
        config=None
    ):


        return self.bridge.generate(

            prompt,

            config

        )

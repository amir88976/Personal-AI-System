"""
Personal AI System
LLM Gateway v3.1
"""


class LLMGateway:


    def __init__(self):

        self.engine = None



    def connect(
        self,
        engine
    ):

        self.engine = engine




    def ask(
        self,
        prompt
    ):


        if self.engine is None:

            return (
                "موتور زبانی هنوز متصل نشده است."
            )



        return self.engine.generate(
            prompt
        )

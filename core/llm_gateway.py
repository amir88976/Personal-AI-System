"""
Personal AI System
LLM Gateway v3.2
"""


from config.ai_config import AIConfig




class LLMGateway:


    def __init__(self):

        self.engine = None

        self.config = AIConfig()



    def connect(
        self,
        engine
    ):

        self.engine = engine




    def ask(
        self,
        prompt
    ):


        if not self.engine:

            return (
                "مدل هوش مصنوعی متصل نیست."
            )



        return self.engine.generate(

            prompt,

            self.config.all()

        )

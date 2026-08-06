"""
Personal AI System
Local AI Engine
"""


from model_server import generate_response



class LocalAIEngine:


    def generate(
        self,
        prompt,
        config=None
    ):

        return generate_response(prompt)

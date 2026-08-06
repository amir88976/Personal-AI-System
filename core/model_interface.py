"""
Personal AI System
Model Interface v3.3
"""


from abc import ABC, abstractmethod




class BaseModel(ABC):


    @abstractmethod
    def generate(
        self,
        prompt,
        config=None
    ):

        pass

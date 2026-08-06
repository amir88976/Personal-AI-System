"""
Personal AI System
AI Provider Manager v2.2
"""


class AIProvider:


    def __init__(self):

        self.providers = {

            "local": None,

            "remote": None

        }


        self.active = "local"



    def set_provider(
            self,
            name,
            provider
    ):

        self.providers[name] = provider



    def generate(
            self,
            prompt
    ):


        provider = self.providers.get(
            self.active
        )


        if provider:

            return provider.generate(
                prompt
            )


        return (
            "هنوز موتور اصلی هوش مصنوعی "
            "متصل نشده است."
        )

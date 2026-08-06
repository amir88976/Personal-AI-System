"""
Personal AI System
Personality Engine v0.3
"""


class PersonalityEngine:


    def __init__(self):

        self.profile = {

            "name": "Personal AI",

            "style": "friendly",

            "tone": "smart",

            "language": "fa"

        }



    def set_personality(self, key, value):

        self.profile[key] = value



    def get_personality(self):

        return self.profile



    def format(self, text):


        style = self.profile.get(
            "style",
            "friendly"
        )


        if style == "friendly":

            return (
                "🤖 "
                + text
            )


        elif style == "professional":

            return (
                "تحلیل سیستم:\n"
                + text
            )


        elif style == "short":

            return text[:300]


        return text



    def introduce(self):

        return (
            f"من {self.profile['name']} هستم. "
            "یک سیستم هوش مصنوعی شخصی."
        )

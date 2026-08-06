"""
Personal AI System
Emotion Engine v1.4
"""


class EmotionEngine:


    def analyze(self, message):

        text = message.lower()



        if any(
            x in text
            for x in [
                "ای بابا",
                "وای",
                "خسته شدم",
                "نمی‌شه",
                "نمیشه"
            ]
        ):

            return "frustrated"



        if any(
            x in text
            for x in [
                "چیکار کنم",
                "کمک",
                "نمیدونم"
            ]
        ):

            return "help"



        if any(
            x in text
            for x in [
                "خوبه",
                "عالیه",
                "دمت گرم"
            ]
        ):

            return "happy"



        return "normal"




    def response(self, emotion):


        if emotion == "frustrated":

            return (
                "می‌فهمم 😅 "
                "یه مشکلی پیش اومده؟ "
                "بگو با هم حلش کنیم."
            )


        if emotion == "help":

            return (
                "من اینجام 👌 "
                "بگو دقیقاً کجا گیر کردی تا بررسی کنیم."
            )


        if emotion == "happy":

            return (
                "خوشحالم که راضی هستی 😊"
            )


        return None

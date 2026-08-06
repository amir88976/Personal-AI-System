"""
Personal AI System
Dialogue Manager v0.7
"""


class DialogueManager:


    def __init__(self):

        self.last_topic = None

        self.mood = "friendly"



    def reply(self, message):

        text = message.lower()



        if "سلام" in text:

            return (
                "سلام 👋😊 "
                "خوش اومدی. "
                "امروز حالت چطوره؟"
            )



        if any(
            x in text
            for x in [
                "خوبم",
                "خوبه",
                "عالی"
            ]
        ):

            return (
                "خوشحالم که خوبی 😊 "
                "من اینجام که کمکت کنم."
            )



        if "خسته" in text:

            return (
                "امیدوارم کمی استراحت کنی. "
                "اگر خواستی می‌تونیم آروم ادامه بدیم."
            )



        if "آره" in text or "بله" in text:

            return (
                "عالیه 👌 "
                "بگو از کجا ادامه بدیم."
            )



        return None

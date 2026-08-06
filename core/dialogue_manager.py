"""
Personal AI System
Dialogue Manager v1.0
"""


class DialogueManager:


    def reply(self, message):

        text = message.lower()



        if "سلام" in text:

            return (
                "سلام حسین 👋😊\n"
                "خوش اومدی. امروز چطوری؟"
            )



        if (
            "خوبم" in text
            or "عالی" in text
        ):

            return (
                "خوشحالم که خوبی 😊\n"
                "امروز روی چی کار کنیم؟"
            )



        if "مرسی" in text or "ممنون" in text:

            return (
                "خواهش می‌کنم 👌"
            )



        return None

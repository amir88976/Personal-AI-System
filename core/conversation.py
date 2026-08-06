"""
Personal AI System
Conversation Engine v0.6

Natural conversation layer
"""


class ConversationEngine:


    def __init__(self):

        self.history = []



    def process(self, message):

        text = message.strip().lower()


        self.history.append(message)



        # سلام

        if any(
            word in text
            for word in [
                "سلام",
                "درود",
                "hello"
            ]
        ):

            return (
                "سلام 👋\n"
                "خوش اومدی. حالت چطوره؟"
            )



        # احوالپرسی

        if any(
            word in text
            for word in [
                "خوبی",
                "حالت چطوره",
                "چه خبر"
            ]
        ):

            return (
                "ممنون که پرسیدی 😊\n"
                "من آماده‌ام کمکت کنم."
            )



        # تشکر

        if "مرسی" in text or "ممنون" in text:

            return (
                "خواهش می‌کنم 👌"
            )



        # خداحافظی

        if "خداحافظ" in text:

            return (
                "فعلاً خداحافظ 👋"
            )



        return None

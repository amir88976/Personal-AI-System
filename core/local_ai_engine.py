"""
Personal AI System
Local AI Engine v3.0
"""


class LocalAIEngine:


    def __init__(self):

        self.model_name = "Personal Brain v3"



    def generate(
        self,
        prompt
    ):


        text = str(prompt)


        lower = text.lower()



        if "سلام" in lower:

            return (
                "سلام حسین 👋😊 "
                "خوش اومدی. چه خبر؟"
            )



        if (
            "هیچی" in lower
            or "هیچ" in lower
        ):

            return (
                "باشه 😊 "
                "گاهی هم هیچی نگفتن خوبه. "
                "الان دوست داری درباره چی حرف بزنیم؟"
            )



        if (
            "چرت و پرت نگو" in lower
            or "مزخرف" in lower
        ):

            return (
                "باشه 😅 سعی می‌کنم بهتر جواب بدم. "
                "بگو دقیقاً چی می‌خوای تا درست‌تر کمکت کنم."
            )



        if "چطوری" in lower:

            return (
                "خوبم، ممنون که پرسیدی 😊 "
                "من اینجام که باهات گفتگو کنم."
            )



        return (
            "پیامت رو گرفتم 👌 "
            "دارم بهتر یاد می‌گیرم که طبیعی‌تر جواب بدم."
        )

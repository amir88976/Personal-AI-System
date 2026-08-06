"""
Personal AI System
Local AI Engine v2.8
"""


class LocalAIEngine:


    def __init__(self):

        self.model_name = "Personal Brain"



    def generate(
        self,
        prompt
    ):


        text = str(prompt).lower()



        if "شعر" in text:

            return """
در دل شب، نوری از امید پیداست،
راهی که می‌رویم همیشه زیباست.
هر قدم کوچک، شروع یک سفر،
فردایی روشن در انتظار ماست.
"""



        if "سلام" in text:

            return (
                "سلام حسین 👋😊 "
                "خوش اومدی، چه خبر؟"
            )



        if "اسم من" in text:

            return (
                "یادم هست که گفتی اسمت حسین است."
            )



        return (
            "پیامت را دریافت کردم. "
            "دارم روی درک بهتر گفتگو کار می‌کنم."
        )

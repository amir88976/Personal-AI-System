"""
Personal AI System
LLM Engine v2.0
"""


class LLMEngine:


    def __init__(self):

        self.system_prompt = """
تو یک دستیار هوش مصنوعی شخصی هستی.
با کاربر دوستانه، طبیعی و با درک گفتگو صحبت کن.
جواب‌ها را رباتی و تکراری نکن.
"""



    def generate(
        self,
        message,
        memory=None
    ):


        # فعلاً جای اتصال مدل واقعی است

        return (
            "دارم روی پاسخ بهتر فکر می‌کنم: "
            + message
        )

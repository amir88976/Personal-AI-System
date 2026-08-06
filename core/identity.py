"""
Personal AI System
Identity Engine v0.9
"""


class IdentityEngine:


    def __init__(self):

        self.name = "Personal AI"



    def check(self, message):

        text = message.lower()



        # پرسش درباره نام AI

        if (
            "اسمت چیه" in text
            or "اسم تو چیه" in text
            or "نام تو" in text
        ):

            return (
                f"من {self.name} هستم 🤖 "
                "دستیار هوش مصنوعی شخصی تو."
            )



        # معرفی کاربر

        if (
            "اسم من" in text
            or "من حسینه" in text
            or "من حسین هستم" in text
        ):

            return (
                "خوشحالم که شناختمت حسین 👋 "
                "اطلاعاتت را به خاطر می‌سپارم."
            )



        return None

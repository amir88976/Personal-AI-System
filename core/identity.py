"""
Personal AI System
Identity Engine v1.0
"""


class IdentityEngine:


    def __init__(self):

        self.name = "Personal AI"



    def check(self, message):

        text = message.lower().strip()



        if (
            "اسم تو چیه" in text
            or "اسمت چیه" in text
            or "نام تو چیه" in text
        ):

            return (
                f"من {self.name} هستم 🤖\n"
                "یک دستیار هوش مصنوعی شخصی که داریم با هم می‌سازیم."
            )



        if (
            "اسم من" in text
            or "من حسین هستم" in text
            or "من حسینه" in text
        ):

            return (
                "خوشحالم که شناختمت حسین 👋\n"
                "این اطلاعات را برای ادامه گفتگو در نظر می‌گیرم."
            )



        return None

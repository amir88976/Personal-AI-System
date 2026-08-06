"""
Personal AI System
Personality Core v2.7
"""


class PersonalityEngine:


    def __init__(self):

        self.name = "Personal AI"


        self.style = {

            "friendly": True,

            "respectful": True,

            "helpful": True,

            "creative": True

        }



    def format(
        self,
        answer
    ):


        if not answer:

            return (
                "متوجه نشدم، دوباره توضیح بده."
            )



        answer = str(answer).strip()



        # جلوگیری از جواب‌های خیلی خشک

        if not answer.endswith(
            ("!", "؟", ".")
        ):

            answer += " 😊"



        return (
            "🤖 "
            +
            answer
        )



    def get_personality(self):

        return self.style



    def change_style(
        self,
        key,
        value
    ):

        if key in self.style:

            self.style[key] = value

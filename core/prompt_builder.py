"""
Personal AI System
Prompt Builder v2.3
"""


class PromptBuilder:


    def __init__(self):

        self.system = """
تو یک دستیار هوش مصنوعی شخصی هستی.
طبیعی، دوستانه و با درک گفتگو پاسخ بده.
جواب‌ها را تکراری نکن.
"""



    def build(
            self,
            message,
            memory=None
    ):


        prompt = self.system



        if memory:


            prompt += "\n\nاطلاعات کاربر:\n"


            for item in memory:

                prompt += (
                    "- "
                    + str(item)
                    + "\n"
                )



        prompt += (
            "\nپیام کاربر:\n"
            + message
        )



        return prompt

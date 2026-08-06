"""
Personal AI System
Prompt Builder v2.3
"""


class PromptBuilder:


    def __init__(self):

        self.system_prompt = """
تو Personal AI هستی.
یک دستیار هوش مصنوعی شخصی هستی.
طبیعی، دوستانه و با درک گفتگو صحبت کن.
جواب‌ها را تکراری و رباتی نکن.
به اطلاعات قبلی کاربر توجه کن.
"""



    def build(
        self,
        message,
        memory=None,
        history=None
    ):


        prompt = self.system_prompt



        if memory:

            prompt += "\n\nاطلاعات کاربر:\n"

            for item in memory:

                prompt += (
                    "- "
                    + str(item)
                    + "\n"
                )



        if history:

            prompt += "\n\nگفتگوی اخیر:\n"

            for item in history:

                prompt += (
                    item["role"]
                    + ": "
                    + item["text"]
                    + "\n"
                )



        prompt += (
            "\nپیام جدید کاربر:\n"
            + message
        )



        return prompt

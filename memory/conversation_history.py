"""
Personal AI System
Conversation History v2.4
"""


from datetime import datetime



class ConversationHistory:


    def __init__(self):

        self.messages = []



    def add(
        self,
        role,
        text
    ):


        self.messages.append({

            "role": role,

            "text": text,

            "time": datetime.now().isoformat()

        })


        # فقط ۳۰ پیام آخر

        if len(self.messages) > 30:

            self.messages.pop(0)




    def get_history(self):

        return self.messages




    def clear(self):

        self.messages = []

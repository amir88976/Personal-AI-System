"""
Personal AI System
Conversation Context Memory v0.8
"""


from datetime import datetime



class ConversationMemory:


    def __init__(self):

        self.history = []



    def add_message(self, role, text):


        self.history.append({

            "role": role,

            "text": text,

            "time": datetime.now().isoformat()

        })



        # نگه داشتن آخرین 50 پیام

        if len(self.history) > 50:

            self.history.pop(0)




    def get_recent(self, count=5):

        return self.history[-count:]




    def get_last_topic(self):


        if not self.history:

            return None


        return self.history[-1]["text"]




    def clear(self):

        self.history = []

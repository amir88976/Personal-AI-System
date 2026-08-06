"""
Personal AI System
Decision Engine v0.3

Request analysis layer
"""


class DecisionEngine:


    def __init__(self):

        self.actions = {

            "question": [
                "چیست",
                "چرا",
                "چطور",
                "چگونه",
                "آیا"
            ],

            "memory": [
                "یادآوری",
                "به خاطر بسپار",
                "فراموش نکن"
            ],

            "planning": [
                "برنامه",
                "هدف",
                "زمان‌بندی"
            ]

        }



    def analyze(self, message):

        text = str(message).lower()


        for category, words in self.actions.items():

            for word in words:

                if word in text:

                    return {

                        "type": category,

                        "confidence": 0.8,

                        "message": message

                    }



        return {

            "type": "conversation",

            "confidence": 0.5,

            "message": message

        }




    def decide(self, message):

        analysis = self.analyze(message)


        if analysis["type"] == "memory":

            return "memory_action"


        if analysis["type"] == "planning":

            return "planning_action"


        if analysis["type"] == "question":

            return "answer_action"


        return "conversation_action"

"""
Personal AI System
Model Server Bridge v3.5
"""


import requests




class ModelServerBridge:


    def __init__(self):

        self.server_url = None

        self.enabled = False




    def connect(
        self,
        url
    ):

        self.server_url = url

        self.enabled = True




    def generate(
        self,
        prompt,
        config=None
    ):


        if not self.enabled:

            return (
                "سرور مدل هنوز وصل نشده است."
            )



        try:

            response = requests.post(

                self.server_url,

                json={

                    "prompt": prompt,

                    "config": config

                },

                timeout=60

            )



            data = response.json()



            return data.get(

                "response",

                "پاسخی دریافت نشد."

            )



        except Exception as e:


            return (
                "خطای اتصال مدل: "
                + str(e)
            )

"""
Personal AI System
Profile Memory v1.1
"""


class ProfileMemory:


    def __init__(self):

        self.profile = {

            "name": None,

            "facts": []

        }



    def learn(self, message):


        text = message.strip()



        if "اسم من" in text:


            name = text.replace(
                "اسم من",
                ""
            ).strip()


            self.profile["name"] = name


            return (
                f"خوشحالم که شناختمت {name} 👋"
            )



        if (
            "من هستم" in text
        ):


            self.profile["facts"].append(
                text
            )


            return (
                "این اطلاعات را به خاطر می‌سپارم."
            )



        return None





    def get_information(self):


        result = []


        if self.profile["name"]:

            result.append(
                "نام: "
                +
                self.profile["name"]
            )



        result.extend(
            self.profile["facts"]
        )


        return result

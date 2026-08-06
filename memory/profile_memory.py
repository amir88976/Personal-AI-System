"""
Personal AI System
Persistent Profile Memory v1.3
"""


from memory.database import Database



class ProfileMemory:


    def __init__(self):

        self.db = Database()



    def learn(self, message):


        text = message.strip()



        # یادگیری اسم


        if "اسم من" in text:


            name = text.replace(
                "اسم من",
                ""
            ).strip()



            self.db.save(
                "name",
                name
            )



            return (
                f"خوشحالم که شناختمت {name} 👋\n"
                "اسمت را به خاطر سپردم."
            )




        # یادگیری اطلاعات دیگر


        if "من هستم" in text:


            self.db.save(
                "fact",
                text
            )


            return (
                "این اطلاعات را ذخیره کردم 🧠"
            )



        return None





    def get_information(self):


        result = []



        names = self.db.get(
            "name"
        )


        facts = self.db.get(
            "fact"
        )



        if names:

            result.append(
                "نام: "
                +
                names[-1]
            )



        result.extend(
            facts
        )



        return result

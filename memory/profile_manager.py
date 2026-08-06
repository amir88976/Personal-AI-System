"""
Personal AI System
User Profile Manager v0.7
"""


class ProfileManager:


    def __init__(self):

        self.fields = {

            "name": None,

            "role": None,

            "interests": [],

            "goals": []

        }



    def set_name(self, name):

        self.fields["name"] = name



    def set_role(self, role):

        self.fields["role"] = role



    def add_interest(self, item):

        self.fields["interests"].append(
            item
        )



    def add_goal(self, goal):

        self.fields["goals"].append(
            goal
        )



    def get_profile(self):

        return self.fields

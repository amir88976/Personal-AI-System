"""
Personal AI System
Smart Router v0.4

Request routing layer
"""


from core.brain import process_brain



def process_request(message):


    try:

        result = process_brain(
            message
        )

        return result


    except Exception as error:


        return (
            "خطا در پردازش مغز AI:\n"
            + str(error)
        )

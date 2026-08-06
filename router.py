"""
Personal AI System
Smart Router v1.0
"""

from brain import think


def process_request(message):

    try:
        return think(message)

    except Exception as error:
        return "خطا در پردازش مغز AI:\n" + str(error)

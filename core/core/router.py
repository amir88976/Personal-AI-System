# Personal AI System
# Core Router
# Version 0.1


from core.brain import think


def process_request(message):

    response = think(message)

    return response

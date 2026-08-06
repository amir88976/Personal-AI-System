# Personal AI System
# Main Entry Point
# Version 0.1


from config.settings import AI_NAME
from core.brain import think


def start():

    print(f"{AI_NAME} is online.")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI shutting down...")
            break

        response = think(user_input)

        print("AI:", response)



if __name__ == "__main__":
    start()

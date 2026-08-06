# Personal AI System
# Main


from settings import AI_NAME
from router import process_request



def start():

    print(AI_NAME, "Online")


    while True:

        user = input("You: ")


        if user == "exit":

            print("Shutdown")

            break


        answer = process_request(user)


        print("AI:", answer)



if __name__ == "__main__":

    start()

# Brain Core


from settings import AI_NAME
from memory_manager import remember



def think(message):

    message = message.lower()


    remember(message)


    if "سلام" in message:

        return f"سلام، من {AI_NAME} هستم."


    elif "اسم" in message:

        return f"اسم من {AI_NAME} است."


    elif "خوبی" in message:

        return "خوبم، در حال توسعه هستم."


    else:

        return "پیام دریافت شد و ذخیره شد."

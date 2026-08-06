# Personal AI System
# Brain Core
# Version 0.1


from config.settings import AI_NAME


def think(message):

    message = message.lower()


    if "سلام" in message or "hello" in message:
        return f"سلام، من {AI_NAME} هستم. آماده‌ام."


    elif "اسم" in message:
        return f"اسم من {AI_NAME} است."


    elif "خوبی" in message:
        return "خوبم. سیستم در حال توسعه است."


    else:
        return "پیام دریافت شد. هنوز در مرحله یادگیری هستم."

"""
Personal AI System
Brain Core v3.6
"""

from settings import AI_NAME
from memory_manager import remember, get_memories


def think(message):

    text = str(message).strip()
    lower = text.lower()

    remember(text)

    memories = get_memories()

    if "سلام" in lower:
        return f"سلام حسین 👋😊 خوش اومدی. من {AI_NAME} هستم، چطوری؟"

    if "اسم من" in lower:
        return "یادم هست گفتی اسمت حسین است."

    if "اسم تو" in lower or "اسمت چیه" in lower:
        return f"من {AI_NAME} هستم 🤖"

    if "شعر" in lower:
        return "در مسیر زندگی، امیدی هست که می‌درخشد، هر قدم کوچک شروع یک راه بزرگ است."

    if "کی هستم" in lower or "من کیم" in lower:
        return "طبق حافظه من، گفتی اسمت حسین است."

    if "چطوری" in lower:
        return "خوبم حسین 😊 آماده‌ام باهات گفتگو کنم."

    if "هیچی" in lower:
        return "باشه 😊 گاهی وقت‌ها هیچی هم خوبه. دوست داری درباره چی حرف بزنیم؟"

    return f"حسین، پیام تو رو گرفتم: {text} 😊"

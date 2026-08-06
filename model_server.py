"""
Personal AI System
Model Server v3.7
"""

from flask import Flask, request, jsonify


app = Flask(__name__)


def generate_response(prompt):

    text = str(prompt).strip()
    lower = text.lower()



    # سلام

    if any(
        word in lower
        for word in [
            "سلام",
            "salam",
            "درود",
            "های",
            "hi"
        ]
    ):

        return (
            "سلام حسین 👋😊 "
            "خوش اومدی. امروز چطوری؟ "
            "چه کاری می‌خوای انجام بدیم؟"
        )



    # احوالپرسی

    if (
        "چطوری" in lower
        or "خوبی" in lower
    ):

        return (
            "خوبم حسین 😊 "
            "آماده‌ام باهات صحبت کنم. "
            "تو چطوری؟"
        )



    # اسم

    if (
        "اسم تو" in lower
        or "اسمت" in lower
    ):

        return (
            "من Personal AI هستم 🤖 "
            "دستیار هوش مصنوعی شخصی تو."
        )



    # اسم کاربر

    if (
        "اسم من" in lower
        or "من کی هستم" in lower
    ):

        return (
            "یادم هست که گفتی اسمت حسین است."
        )



    # ناراحتی

    if (
        "ای بابا" in lower
        or "خسته" in lower
    ):

        return (
            "چی شده حسین؟ 😊 "
            "اگر چیزی اذیتت کرده بگو، گوش می‌کنم."
        )



    # خداحافظی

    if (
        "خداحافظ" in lower
        or "فعلا" in lower
    ):

        return (
            "باشه حسین 👋 "
            "هر وقت خواستی دوباره برگرد."
        )



    # جواب عمومی بهتر

    return (
        "جالبه حسین 😊 "
        "دارم گوش می‌کنم. "
        "بیشتر برام توضیح بده."
    )




@app.route(
    "/generate",
    methods=["POST"]
)
def generate():


    data = request.json or {}


    prompt = data.get(
        "prompt",
        ""
    )


    answer = generate_response(
        prompt
    )


    return jsonify({

        "response": answer

    })





if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5001

    )

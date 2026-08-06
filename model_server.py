"""
Personal AI System
Model Server v3.6
"""


from flask import Flask, request, jsonify



app = Flask(__name__)



@app.route(
    "/generate",
    methods=["POST"]
)
def generate():


    data = request.json


    prompt = data.get(
        "prompt",
        ""
    )



    answer = create_response(
        prompt
    )


    return jsonify({

        "response": answer

    })





def create_response(prompt):


    text = prompt.lower()



    if "سلام" in text:

        return (
            "سلام حسین 👋😊 "
            "خوش اومدی، حالت چطوره؟"
        )



    if "اسم من" in text:

        return (
            "یادم هست گفتی اسمت حسین است."
        )



    if "شعر" in text:

        return (
            "در دل شب نور امیدی هست، "
            "هر قدم آغاز راهی تازه است."
        )



    return (
        "پیامت رو دریافت کردم حسین. "
        "دارم بهتر یاد می‌گیرم که طبیعی‌تر گفتگو کنم."
    )





if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001
    )

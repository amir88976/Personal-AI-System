"""
Personal AI System
Router v2.0
"""

try:
    from brain import process_brain

except ImportError:

    from brain import think as process_brain





def analyze_request(
    text
):

    """
    مسیر اصلی پردازش پیام
    """

    try:

        response = process_brain(
            text
        )

        return response


    except Exception as error:

        return (
            "خطا در هسته هوش مصنوعی:\n"
            + str(error)
        )





def process_request(
    text
):

    return analyze_request(
        text
    )

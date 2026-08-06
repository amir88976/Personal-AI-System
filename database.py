# Memory Database

import json
import os

from settings import MEMORY_FILE


def initialize_memory():

    if not os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                ensure_ascii=False
            )


def load_memory():

    initialize_memory()

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_memory(data):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

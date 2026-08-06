"""
Personal AI System
Chat Database v2.5
"""


import sqlite3

from datetime import datetime



class ChatDatabase:


    def __init__(self):

        self.db = sqlite3.connect(
            "personal_ai_chat.db",
            check_same_thread=False
        )

        self.create_table()




    def create_table(self):


        cursor = self.db.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS chat_history
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                message TEXT,
                time TEXT
            )
            """
        )


        self.db.commit()




    def save(
        self,
        role,
        message
    ):


        cursor = self.db.cursor()


        cursor.execute(
            """
            INSERT INTO chat_history
            (
                role,
                message,
                time
            )
            VALUES (?, ?, ?)
            """,
            (
                role,
                message,
                datetime.now().isoformat()
            )
        )


        self.db.commit()




    def load(
        self,
        limit=20
    ):


        cursor = self.db.cursor()


        cursor.execute(
            """
            SELECT role,message,time
            FROM chat_history
            ORDER BY id DESC
            LIMIT ?
            """,
            (
                limit,
            )
        )


        rows = cursor.fetchall()


        rows.reverse()


        return [

            {
                "role": r[0],
                "text": r[1],
                "time": r[2]
            }

            for r in rows

        ]

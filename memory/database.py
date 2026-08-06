"""
Personal AI System
SQLite Memory Database v1.2
"""


import sqlite3



class Database:


    def __init__(self):

        self.connection = sqlite3.connect(
            "personal_ai_memory.db",
            check_same_thread=False
        )


        self.create_tables()



    def create_tables(self):


        cursor = self.connection.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                content TEXT
            )
            """
        )


        self.connection.commit()




    def save(
            self,
            category,
            content
    ):


        cursor = self.connection.cursor()


        cursor.execute(
            """
            INSERT INTO memories
            (category, content)
            VALUES (?, ?)
            """,
            (
                category,
                content
            )
        )


        self.connection.commit()




    def get(
            self,
            category=None
    ):


        cursor = self.connection.cursor()



        if category:


            cursor.execute(
                """
                SELECT content
                FROM memories
                WHERE category=?
                """,
                (
                    category,
                )
            )


        else:


            cursor.execute(
                """
                SELECT content
                FROM memories
                """
            )



        return [
            row[0]
            for row in cursor.fetchall()
        ]

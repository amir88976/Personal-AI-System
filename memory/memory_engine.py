import sqlite3
import os
import datetime


DATABASE = "memory.db"


class MemoryEngine:

    def __init__(self):

        self.connection = sqlite3.connect(
            DATABASE,
            check_same_thread=False
        )

        self.create_tables()


    def create_tables(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            content TEXT NOT NULL,

            category TEXT DEFAULT 'general',

            created_at TEXT

        )
        """)

        self.connection.commit()



    def remember(self, content, category="general"):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO memories
            (content, category, created_at)

            VALUES (?, ?, ?)
            """,
            (
                content,
                category,
                str(datetime.datetime.now())
            )
        )

        self.connection.commit()

        return True



    def recall(self, keyword=None):

        cursor = self.connection.cursor()


        if keyword:

            cursor.execute(
                """
                SELECT content, category
                FROM memories
                WHERE content LIKE ?
                ORDER BY id DESC
                """,
                (
                    f"%{keyword}%",
                )
            )

        else:

            cursor.execute(
                """
                SELECT content, category
                FROM memories
                ORDER BY id DESC
                """
            )


        return cursor.fetchall()



    def get_recent(self, limit=10):

        cursor = self.connection.cursor()


        cursor.execute(
            """
            SELECT content, category
            FROM memories
            ORDER BY id DESC
            LIMIT ?
            """,
            (
                limit,
            )
        )


        return cursor.fetchall()

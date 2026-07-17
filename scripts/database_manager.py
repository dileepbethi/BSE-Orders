"""
Database Manager
Version: 1.0

Creates and manages the SQLite database.
"""

import sqlite3
from pathlib import Path


DATABASE_FOLDER = Path("database")
DATABASE_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_FILE = DATABASE_FOLDER / "bse_orders.db"


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(DATABASE_FILE)

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS orders (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            company TEXT,

            announcement_date TEXT,

            awarding_entity TEXT,

            order_value TEXT,

            execution_period TEXT,

            order_type TEXT,

            domestic TEXT,

            project_description TEXT,

            source_file TEXT UNIQUE,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.connection.commit()

    def insert(self, record):

        self.cursor.execute("""

        INSERT OR REPLACE INTO orders (

            company,
            announcement_date,
            awarding_entity,
            order_value,
            execution_period,
            order_type,
            domestic,
            project_description,
            source_file

        )

        VALUES (

            ?, ?, ?, ?, ?, ?, ?, ?, ?

        )

        """, (

            record["company"],
            record["announcement_date"],
            record["awarding_entity"],
            record["order_value"],
            record["execution_period"],
            record["order_type"],
            record["domestic"],
            record["project_description"],
            record["source_file"]

        ))

        self.connection.commit()

    def count(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM orders"
        )

        return self.cursor.fetchone()[0]


    def get_all(self):

        self.cursor.execute("""

            SELECT *

            FROM orders

            ORDER BY announcement_date DESC

        """)

        return self.cursor.fetchall()


    def find_company(self, company):

        self.cursor.execute("""

            SELECT *

            FROM orders

            WHERE company LIKE ?

            ORDER BY announcement_date DESC

        """, (f"%{company}%",))

        return self.cursor.fetchall()


    def latest(self, limit=20):

        self.cursor.execute("""

            SELECT *

            FROM orders

            ORDER BY created_at DESC

            LIMIT ?

        """, (limit,))

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()
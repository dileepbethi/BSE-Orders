"""
Database Manager V2

Production-ready SQLite manager
for the BSE Orders pipeline.
"""

import sqlite3
from pathlib import Path


DATABASE_FOLDER = Path("data/database")
DATABASE_FILE = DATABASE_FOLDER / "bse_orders.db"


class DatabaseManagerV2:

    def __init__(self):

        DATABASE_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            DATABASE_FILE
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()
    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                source_file TEXT UNIQUE,

                company TEXT,

                announcement_date TEXT,

                awarding_entity TEXT,

                order_value TEXT,

                execution_period TEXT,

                order_type TEXT,

                domestic TEXT,

                project_description TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.connection.commit()
    def insert(self, record: dict):
        """
        Inserts a record into the database.

        If the source_file already exists,
        the record is ignored.
        """

        self.cursor.execute(
            """
            INSERT OR IGNORE INTO orders (

                source_file,
                company,
                announcement_date,
                awarding_entity,
                order_value,
                execution_period,
                order_type,
                domestic,
                project_description

            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record.get("source_file"),
                record.get("company"),
                record.get("announcement_date"),
                record.get("awarding_entity"),
                record.get("order_value"),
                record.get("execution_period"),
                record.get("order_type"),
                record.get("domestic"),
                record.get("project_description"),
            )
        )

        self.connection.commit()
    def count(self) -> int:
        """
        Returns the total number of records.
        """

        self.cursor.execute(
            "SELECT COUNT(*) FROM orders"
        )

        return self.cursor.fetchone()[0]

    def fetch_all(self):
        """
        Returns all records.
        """

        self.cursor.execute(
            """
            SELECT *
            FROM orders
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()


def main():

    db = DatabaseManagerV2()

    print("=" * 50)
    print("DATABASE MANAGER V2")
    print("=" * 50)
    print(f"Current Records : {db.count()}")

    db.close()


if __name__ == "__main__":

    main()
"""
OrderIQ Database Manager
Production Version
"""

import sqlite3
from pathlib import Path


DB_FILE = Path("database/bse_orders_v2.db")


class DatabaseManager:

    def __init__(self):

        DB_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = sqlite3.connect(DB_FILE)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS announcements(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company TEXT,

                customer TEXT,

                announcement_date TEXT,

                announcement_type TEXT,

                order_value TEXT,

                order_value_crore REAL,

                awarding_entity TEXT,

                execution_period TEXT,

                order_type TEXT,

                domestic TEXT,

                project_description TEXT,

                source_file TEXT UNIQUE,

                exchange TEXT,

                confidence_score REAL,

                processing_status TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.connection.commit()

    def insert_record(
        self,
        record: dict
    ):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO announcements(

                company,
                customer,
                announcement_date,
                announcement_type,
                order_value,
                order_value_crore,
                awarding_entity,
                execution_period,
                order_type,
                domestic,
                project_description,
                source_file,
                exchange,
                confidence_score,
                processing_status

            )

            VALUES(

                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?

            )
            """,
            (

                record.get("company", ""),

                record.get("customer", ""),

                record.get("announcement_date", ""),

                record.get("announcement_type", ""),

                record.get("order_value", ""),

                record.get("order_value_crore", 0.0),

                record.get("awarding_entity", ""),

                record.get("execution_period", ""),

                record.get("order_type", ""),

                record.get("domestic", ""),

                record.get("project_description", ""),

                record.get("source_file", ""),

                record.get("exchange", "BSE"),

                record.get("confidence_score", 1.0),

                record.get("processing_status", "SUCCESS")

            )
        )

        self.connection.commit()

    # Backward compatibility
    def insert(self, record):

        self.insert_record(record)

    def count(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM announcements
            """
        )

        return self.cursor.fetchone()[0]

    def get_all_records(self):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()
"""
OrderIQ Database Manager

Sprint 3
Version: 1.0
"""

import sqlite3


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/bse_orders.db"
        )

        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS announcements (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                company TEXT,

                customer TEXT,

                announcement_date TEXT,

                announcement_type TEXT,

                order_value TEXT,

                source_file TEXT UNIQUE,

                exchange TEXT DEFAULT 'BSE',

                confidence_score REAL DEFAULT 0.0,

                processing_status TEXT DEFAULT 'SUCCESS',

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.connection.commit()

    def insert_record(self, record: dict):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO announcements (

                company,
                customer,
                announcement_date,
                announcement_type,
                order_value,
                source_file,
                exchange,
                confidence_score,
                processing_status

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (

                record.get("company", ""),

                record.get("customer", ""),

                record.get("announcement_date", ""),

                record.get("announcement_type", ""),

                record.get("order_value", ""),

                record.get("source_file", ""),

                record.get("exchange", "BSE"),

                record.get("confidence_score", 1.0),

                record.get("processing_status", "SUCCESS")

            )
        )

        self.connection.commit()

    def get_all_records(self):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            ORDER BY id
            """
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()
        
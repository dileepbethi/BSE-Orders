"""
Database Manager
Version: 3.0

Responsible for:

- Database creation
- Inserts
- Search
- Dashboard statistics
- Dashboard charts
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

    # =====================================================
    # DATABASE SETUP
    # =====================================================

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

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, record):

        self.cursor.execute("""

        INSERT OR IGNORE INTO orders (

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

    # =====================================================
    # BASIC METHODS
    # =====================================================

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
    # =====================================================
    # DASHBOARD METHODS
    # =====================================================

    def get_total_orders(self):

        return self.count()

    def get_total_companies(self):

        self.cursor.execute("""

            SELECT COUNT(DISTINCT company)

            FROM orders

        """)

        return self.cursor.fetchone()[0]

    def get_domestic_orders(self):

        self.cursor.execute("""

            SELECT COUNT(*)

            FROM orders

            WHERE LOWER(domestic) = 'domestic'

        """)

        return self.cursor.fetchone()[0]

    def get_international_orders(self):

        self.cursor.execute("""

            SELECT COUNT(*)

            FROM orders

            WHERE LOWER(domestic) = 'international'

        """)

        return self.cursor.fetchone()[0]

    def get_monthly_orders(self):

        self.cursor.execute("""

            SELECT
                SUBSTR(announcement_date, 6, 2) AS month,
                COUNT(*) AS total

            FROM orders

            WHERE announcement_date IS NOT NULL
              AND announcement_date != ''

            GROUP BY month

            ORDER BY month

        """)

        rows = self.cursor.fetchall()

        month_names = {
            "01": "Jan",
            "02": "Feb",
            "03": "Mar",
            "04": "Apr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Aug",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec",
        }

        result = []

        for month, total in rows:

            result.append({
                "month": month_names.get(month, month),
                "value": total
            })

        return result

    # =====================================================
    # CONNECTION METHODS
    # =====================================================

    def get_connection(self):

        return self.connection

    def close(self):

        self.connection.close()
"""
OrderIQ Search Engine

Sprint 5
Version: 1.0
"""

import sqlite3


class SearchEngine:

    def __init__(self):

        self.connection = sqlite3.connect(
            "database/bse_orders_v2.db"
        )

        self.cursor = self.connection.cursor()

    # =====================================================
    # SEARCH COMPANY
    # =====================================================

    def search_company(self, company: str):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE company LIKE ?
            ORDER BY announcement_date DESC
            """,
            (f"%{company}%",)
        )

        return self.cursor.fetchall()

    # =====================================================
    # SEARCH CUSTOMER
    # =====================================================

    def search_customer(self, customer: str):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE customer LIKE ?
            ORDER BY announcement_date DESC
            """,
            (f"%{customer}%",)
        )

        return self.cursor.fetchall()

    # =====================================================
    # SEARCH DATE
    # =====================================================

    def search_date(self, date: str):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE announcement_date = ?
            ORDER BY company
            """,
            (date,)
        )

        return self.cursor.fetchall()

    # =====================================================
    # GET ALL
    # =====================================================

    def get_all(self):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            ORDER BY announcement_date DESC
            """
        )

        return self.cursor.fetchall()

    # =====================================================
    # GLOBAL SEARCH
    # =====================================================

    def search(self, query: str):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE company LIKE ?
               OR customer LIKE ?
            ORDER BY announcement_date DESC
            """,
            (
                f"%{query}%",
                f"%{query}%"
            )
        )

        return self.cursor.fetchall()

    # =====================================================
    # CLOSE
    # =====================================================

    def close(self):

        self.connection.close()
    def get_total_records(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM announcements"
        )

        return self.cursor.fetchone()[0]

    def get_total_companies(self):

        self.cursor.execute(
            """
            SELECT COUNT(DISTINCT company)
            FROM announcements
            """
        )

        return self.cursor.fetchone()[0]

    def get_total_customers(self):

        self.cursor.execute(
            """
            SELECT COUNT(DISTINCT customer)
            FROM announcements
            """
        )

        return self.cursor.fetchone()[0]

    def get_total_orders(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM announcements
            WHERE announcement_type='ORDER'
            """
        )

        return self.cursor.fetchone()[0]
    def get_orders_page(self, page: int = 1, limit: int = 20):
        offset = (page - 1) * limit

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            ORDER BY announcement_date DESC
            LIMIT ? OFFSET ?
            """,
            (limit, offset)
        )

        return self.cursor.fetchall()
    def get_all_orders(self):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            ORDER BY announcement_date DESC
            """
        )

        return self.cursor.fetchall()

    # =====================================================
    # UPDATE ORDER
    # =====================================================

    def update_order(self, order_id: int, data: dict):

        self.cursor.execute(
            """
            UPDATE announcements
            SET
                company = ?,
                customer = ?,
                awarding_entity = ?,
                order_value = ?,
                order_value_crore = ?,
                execution_period = ?,
                order_type = ?,
                domestic = ?,
                project_description = ?
            WHERE id = ?
            """,
            (
                data["company"],
                data["customer"],
                data["awarding_entity"],
                data["order_value"],
                data["order_value_crore"],
                data["execution_period"],
                data["order_type"],
                data["domestic"],
                data["project_description"],
                order_id,
            ),
        )

        self.connection.commit()

    # =====================================================
    # GET SINGLE ORDER
    # =====================================================

    def get_order(self, order_id: int):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE id = ?
            """,
            (order_id,)
        )

        return self.cursor.fetchone()
    # =====================================================
    # MONTHLY ORDER TREND
    # =====================================================

    def get_monthly_orders(self):

        self.cursor.execute(
            """
            SELECT
                substr(announcement_date, 1, 7) AS month,
                COUNT(*) AS total
            FROM announcements
            WHERE announcement_type = 'ORDER'
            GROUP BY substr(announcement_date, 1, 7)
            ORDER BY month
            """
        )

        rows = self.cursor.fetchall()

        result = []

        for row in rows:

            result.append({
                "month": row[0],
                "value": row[1]
            })

        return result
    # =====================================================
    # DOMESTIC ORDERS
    # =====================================================

    def get_domestic_orders(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM announcements
            WHERE LOWER(domestic) = 'domestic'
            """
        )

        return self.cursor.fetchone()[0]


    # =====================================================
    # INTERNATIONAL ORDERS
    # =====================================================

    def get_international_orders(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM announcements
            WHERE LOWER(domestic) = 'international'
            """
        )

        return self.cursor.fetchone()[0]


    # =========================================
    # REVIEWS
    # =========================================

    def get_pending_reviews(self):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE processing_status='SUCCESS'
            ORDER BY created_at DESC
            """
        )

        return self.cursor.fetchall()

    def get_review(self, review_id: int):

        self.cursor.execute(
            """
            SELECT *
            FROM announcements
            WHERE id = ?
            """,
            (review_id,)
        )

        return self.cursor.fetchone()
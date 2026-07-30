"""
OrderIQ API

Sprint 6
Version: 2.0
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.search_engine import SearchEngine

app = FastAPI(
    title="OrderIQ API",
    description="Corporate Order Intelligence Platform API",
    version="2.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# ROOT
# ==========================================================

@app.get("/")
def home():

    return {
        "application": "OrderIQ",
        "version": "2.0.0",
        "status": "running"
    }


# ==========================================================
# HEALTH
# ==========================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ==========================================================
# DATABASE STATS
# ==========================================================

@app.get("/stats")
def stats():

    search = SearchEngine()

    data = {

        "total_records": search.get_total_records(),

        "total_companies": search.get_total_companies(),

        "total_customers": search.get_total_customers(),

        "total_orders": search.get_total_orders()

    }

    search.close()

    return data


# ==========================================================
# SEARCH COMPANY
# ==========================================================

@app.get("/search/company/{company}")
def search_company(company: str):

    search = SearchEngine()

    rows = search.search_company(company)

    search.close()

    results = []

    for row in rows:

        results.append({

            "id": row[0],

            "company": row[1],

            "customer": row[2],

            "announcement_date": row[3],

            "announcement_type": row[4],

            "order_value": row[5],

            "source_file": row[6],

            "exchange": row[7],

            "confidence_score": row[8],

            "processing_status": row[9],

            "created_at": row[10]

        })

    return results


# ==========================================================
# SEARCH CUSTOMER
# ==========================================================

@app.get("/search/customer/{customer}")
def search_customer(customer: str):

    search = SearchEngine()

    rows = search.search_customer(customer)

    search.close()

    results = []

    for row in rows:

        results.append({

            "id": row[0],

            "company": row[1],

            "customer": row[2],

            "announcement_date": row[3],

            "announcement_type": row[4],

            "order_value": row[5],

            "source_file": row[6],

            "exchange": row[7],

            "confidence_score": row[8],

            "processing_status": row[9],

            "created_at": row[10]

        })

    return results


# ==========================================================
# SEARCH DATE
# ==========================================================

@app.get("/search/date/{date}")
def search_date(date: str):

    search = SearchEngine()

    rows = search.search_date(date)

    search.close()

    results = []

    for row in rows:

        results.append({

            "id": row[0],

            "company": row[1],

            "customer": row[2],

            "announcement_date": row[3],

            "announcement_type": row[4],

            "order_value": row[5],

            "source_file": row[6],

            "exchange": row[7],

            "confidence_score": row[8],

            "processing_status": row[9],

            "created_at": row[10]

        })

    return results
# ==========================================================
# ALL ORDERS
# ==========================================================

@app.get("/orders")
def get_orders(
    page: int = 1,
    limit: int = 20
):

    search = SearchEngine()

    rows = search.get_all_orders()

    search.close()

    results = []

    for row in rows:

        results.append({

            "id": row[0],

            "company": row[1],

            "customer": row[2],

            "announcement_date": row[3],

            "announcement_type": row[4],

            "order_value": row[5],

            "source_file": row[6],

            "exchange": row[7],

            "confidence_score": row[8],

            "processing_status": row[9],

            "created_at": row[10]

        })

    return results
@app.get("/search")
def search_orders(query: str):

    search = SearchEngine()

    rows = search.search(query)

    search.close()

    orders = []

    for row in rows:

        orders.append({

            "id": row[0],
            "company": row[1],
            "customer": row[2],
            "announcement_date": row[3],
            "announcement_type": row[4],
            "order_value": row[5],
            "source_file": row[6],
            "exchange": row[7],
            "confidence_score": row[8],
            "processing_status": row[9],
            "created_at": row[10]

        })

    return orders
# =====================================================
# GET SINGLE ORDER
# =====================================================

@app.get("/orders/{order_id}")
def get_order(order_id: int):

    search = SearchEngine()

    row = search.get_order(order_id)

    search.close()

    if row is None:
        return {"error": "Order not found"}

    return {

        "id": row[0],
        "company": row[1],
        "customer": row[2],
        "announcement_date": row[3],
        "announcement_type": row[4],
        "order_value": row[5],
        "source_file": row[6],
        "exchange": row[7],
        "confidence_score": row[8],
        "processing_status": row[9],
        "created_at": row[10]

    }
# =====================================================
# DASHBOARD STATS
# =====================================================

@app.get("/dashboard/stats")
def dashboard_stats():

    search = SearchEngine()

    data = {
        "total_orders": search.get_total_orders(),
        "total_companies": search.get_total_companies(),

        # Temporary values until these are calculated properly
        "domestic_orders": 0,
        "international_orders": 0,
    }

    search.close()

    return data


# =====================================================
# MONTHLY ORDER TREND
# =====================================================

# =====================================================
# MONTHLY ORDER TREND
# =====================================================

@app.get("/dashboard/monthly-orders")
def monthly_orders():

    search = SearchEngine()

    data = search.get_monthly_orders()

    search.close()

    return data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.database_manager import DatabaseManager


app = FastAPI(
    title="BSE Orders API",
    description="API for BSE Corporate Orders Dashboard",
    version="1.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "Welcome to BSE Orders API",
        "status": "running"
    }


@app.get("/orders")
def get_orders():

    db = DatabaseManager()

    rows = db.get_all()

    db.close()

    orders = []

    for row in rows:

        orders.append({
            "id": row[0],
            "company": row[1],
            "announcement_date": row[2],
            "awarding_entity": row[3],
            "order_value": row[4],
            "execution_period": row[5],
            "order_type": row[6],
            "domestic": row[7],
            "project_description": row[8],
            "source_file": row[9],
            "created_at": row[10]
        })

    return orders


@app.get("/dashboard/stats")
def dashboard_stats():

    db = DatabaseManager()

    stats = {
        "total_orders": db.get_total_orders(),
        "total_companies": db.get_total_companies(),
        "domestic_orders": db.get_domestic_orders(),
        "international_orders": db.get_international_orders()
    }

    db.close()

    return stats


@app.get("/dashboard/latest-orders")
def latest_orders():

    db = DatabaseManager()

    rows = db.latest(10)

    db.close()

    orders = []

    for row in rows:

        orders.append({
            "id": row[0],
            "company": row[1],
            "announcement_date": row[2],
            "awarding_entity": row[3],
            "order_value": row[4],
            "execution_period": row[5],
            "order_type": row[6],
            "domestic": row[7],
            "project_description": row[8],
            "source_file": row[9],
            "created_at": row[10]
        })

    return orders


@app.get("/dashboard/monthly-orders")
def monthly_orders():

    db = DatabaseManager()

    data = db.get_monthly_orders()

    db.close()

    return data
from flask import Flask, render_template, request, redirect, send_from_directory
from pathlib import Path
from urllib.parse import quote_plus
import json

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

REVIEW_DIR = BASE_DIR / "data" / "gold_review"
DOWNLOAD_DIR = BASE_DIR / "data" / "downloads"


def get_review_files():
    return sorted(REVIEW_DIR.glob("*.json"))


def load_record(file):
    with open(file, "r", encoding="utf-8") as f:
        record = json.load(f)

    if "review_status" not in record:
        record["review_status"] = "Pending"

    return record


def company_links(company_name):

    if not company_name:
        company_name = ""

    query = quote_plus(company_name)

    return {
        "screener": f"https://www.screener.in/company/?q={query}",
        "bse": f"https://www.bseindia.com/stock-share-price/search.aspx?query={query}",
        "nse": f"https://www.nseindia.com/search?query={query}",
    }


def get_missing_fields(record):

    fields = {
        "Company": record.get("company"),
        "Announcement Date": record.get("announcement_date"),
        "Awarding Entity": record.get("awarding_entity"),
        "Order Value": record.get("order_value"),
        "Execution Period": record.get("execution_period"),
        "Order Type": record.get("order_type"),
        "Domestic / International": record.get("domestic"),
    }

    missing = []

    for name, value in fields.items():

        if value is None:
            missing.append(name)
            continue

        value = str(value).strip()

        if value == "":
            missing.append(name)
            continue

        if value.lower() in ["unknown", "na", "n/a", "not available"]:
            missing.append(name)

    return missing
def get_review_score(record):

    total_fields = 7

    missing = len(get_missing_fields(record))

    completed = total_fields - missing

    score = round((completed / total_fields) * 100)

    stars = round(score / 20)

    return {
        "score": score,
        "stars": stars,
    }


def count_reviewed(files):

    reviewed = 0

    for file in files:

        try:
            data = load_record(file)

            if data.get("review_status") == "Reviewed":
                reviewed += 1

        except Exception:
            pass

    return reviewed


def get_dashboard_stats(files):

    total = len(files)

    reviewed = count_reviewed(files)

    pending = total - reviewed

    total_score = 0

    for file in files:
        record = load_record(file)
        total_score += get_review_score(record)["score"]

    average_quality = round(total_score / total) if total else 0

    completion = round((reviewed / total) * 100) if total else 0

    return {
        "total": total,
        "reviewed": reviewed,
        "pending": pending,
        "completion": completion,
        "average_quality": average_quality,
    }


def build_company_list(files):

    companies = []

    for i, file in enumerate(files):

        try:
            data = load_record(file)

            companies.append(
                {
                    "index": i,
                    "company": data.get("company", "Unknown Company"),
                    "status": data.get("review_status", "Pending"),
                }
            )

        except Exception:
            pass

    return companies
@app.route("/", methods=["GET", "POST"])
def home():

    files = get_review_files()

    total = len(files)

    if total == 0:
        return "No review files found."

    index = request.args.get("index", 0, type=int)

    if request.method == "POST":

        index = int(request.form["index"])

        file = files[index]

        record = load_record(file)

        record["company"] = request.form["company"]
        record["announcement_date"] = request.form["announcement_date"]
        record["awarding_entity"] = request.form["awarding_entity"]
        record["order_value"] = request.form["order_value"]
        record["execution_period"] = request.form["execution_period"]
        record["order_type"] = request.form["order_type"]
        record["domestic"] = request.form["domestic"]
        record["review_status"] = request.form["review_status"]

        with open(file, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=4, ensure_ascii=False)

        return redirect(f"/?index={index}")

    if index < 0:
        index = 0

    if index >= total:
        index = total - 1

    record = load_record(files[index])
    pdf_filename = files[index].stem + ".pdf"
    pdf_url = f"/pdf/{pdf_filename}"
    return render_template(
        "index.html",
        record=record,
        current=index + 1,
        total=total,
        index=index,
        has_previous=index > 0,
        has_next=index < total - 1,
        reviewed_count=count_reviewed(files),
        progress_percent=round((count_reviewed(files) / total) * 100) if total else 0,
        company_list=build_company_list(files),
        links=company_links(record.get("company", "")),
        missing_fields=get_missing_fields(record),
        review_score=get_review_score(record),
        dashboard=get_dashboard_stats(files),
        pdf_url=pdf_url,
    )
@app.route("/pdf/<filename>")
def view_pdf(filename):
    return send_from_directory(DOWNLOAD_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
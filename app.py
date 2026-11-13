from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import date

app = Flask(__name__)

DATA_FILE = "expenses.json"

CATEGORIES = [
    "Food",
    "Transport",
    "School",
    "Work",
    "Leisure",
    "Other"
]


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


@app.route("/")
def home():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        categories=CATEGORIES
    )


@app.route("/add", methods=["POST"])
def add_expense():
    item = request.form.get("item", "").strip()
    category = request.form.get("category", "").strip()

    try:
        amount = float(request.form.get("amount", ""))
    except ValueError:
        return redirect(url_for("home"))

    if not item or category not in CATEGORIES:
        return redirect(url_for("home"))

    if amount < 0 or amount != amount or amount == float("inf"):
        return redirect(url_for("home"))

    expenses = load_expenses()

    expenses.append({
        "item": item,
        "amount": amount,
        "category": category,
        "date": date.today().isoformat()
    })

    save_expenses(expenses)

    return redirect(url_for("home"))


@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index):
    expenses = load_expenses()

    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

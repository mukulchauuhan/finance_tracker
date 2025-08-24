# services/report_service.py
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Optional
from services.export_service import export_to_csv, export_report_to_pdf


def prepare_expense_dataframe(expenses: List[Dict]) -> pd.DataFrame:
    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])
    return df


def generate_category_report(
    expenses: List[Dict],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    export_csv=False,
    export_pdf=False,
):
    if not expenses:
        print("No expenses found.")
        return

    df = prepare_expense_dataframe(expenses)

    if start_date:
        df = df[df["date"] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df["date"] <= pd.to_datetime(end_date)]

    if df.empty:
        print("No expenses found in the specified date range.")
        return

    category_totals = (
        df.groupby("category")["amount"].sum().sort_values(ascending=False)
    )

    print("\n--- Spending by Category ---")
    for category, total in category_totals.items():
        print(f"{str(category).title()}: ${total:.2f}")

    if export_csv:
        export_to_csv(category_totals.to_frame(), "category_report.csv")

    if export_pdf:
        export_report_to_pdf(
            "Spending by Category Report",
            category_totals.to_dict(),
            "category_report.pdf",
        )


def generate_monthly_report(
    expenses: List[Dict],
    year: Optional[int] = None,
    export_csv=False,
):
    if not expenses:
        print("No expenses found.")
        return

    df = prepare_expense_dataframe(expenses)

    if year:
        df = df[df["date"].dt.year == year]

    monthly_totals = (
        df.groupby(df["date"].dt.to_period("M"))["amount"].sum().sort_index()
    )

    print(f"\n--- Monthly Spending Report{' for ' + str(year) if year else ''} ---")
    for period, total in monthly_totals.items():
        print(f"{period}: ${total:.2f}")

    if export_csv:
        export_to_csv(monthly_totals.to_frame(), "monthly_totals.csv")


def generate_weekly_report(
    expenses: List[Dict],
    year: Optional[int] = None,
    export_csv=False,
):
    if not expenses:
        print("No expenses found.")
        return

    df = prepare_expense_dataframe(expenses)

    if year:
        df = df[df["date"].dt.year == year]

    weekly_totals = (
        df.groupby(df["date"].dt.to_period("W"))["amount"].sum().sort_index()
    )

    print(f"\n--- Weekly Spending Report{' for ' + str(year) if year else ''} ---")
    for period, total in weekly_totals.items():
        print(f"{period}: ${total:.2f}")

    if export_csv:
        export_to_csv(weekly_totals.to_frame(), "weekly_totals.csv")


def generate_average_report(
    expenses: List[Dict],
    export_csv=False,
):
    if not expenses:
        print("No expenses found.")
        return

    df = prepare_expense_dataframe(expenses)

    avg_by_category = (
        df.groupby("category")["amount"].mean().sort_values(ascending=False)
    )

    print("\n--- Average Spending by Category ---")
    for category, avg in avg_by_category.items():
        print(f"{str(category).title()}: ${avg:.2f}")

    if export_csv:
        export_to_csv(avg_by_category.to_frame(), "avg_by_category.csv")


def plot_category_pie_chart(expenses: List[Dict]):
    if not expenses:
        print("No expenses found.")
        return

    df = prepare_expense_dataframe(expenses)
    category_totals = df.groupby("category")["amount"].sum()

    category_totals.plot.pie(autopct="%1.1f%%", startangle=140)  # type: ignore

    plt.title("Spending by Category")
    plt.ylabel("")  # Hide y-label for better look
    plt.tight_layout()
    plt.show()


def plot_monthly_bar_chart(expenses: List[Dict], year: Optional[int] = None):
    if not expenses:
        print("No expenses found.")
        return

    df = prepare_expense_dataframe(expenses)

    if year:
        df = df[df["date"].dt.year == year]

    monthly_totals = (
        df.groupby(df["date"].dt.to_period("M"))["amount"].sum().sort_index()
    )

    monthly_totals.plot.bar()
    plt.title(f'Monthly Spending{" in " + str(year) if year else ""}')
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.tight_layout()
    plt.show()

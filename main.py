from services.expense_service import ExpenseService
from models.expense import Expense
from models.budget import Budget
from services.report_service import (
    generate_category_report,
    generate_monthly_report,
    generate_weekly_report,
    generate_average_report,
    plot_category_pie_chart,
    plot_monthly_bar_chart,
)
from services.export_service import (
    export_to_csv,
    export_report_to_pdf,
)  # Import export functions


def add_expense(expense_service, budget):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").lower()
    description = input("Enter description: ")

    total_spent = sum(
        e.amount for e in expense_service.get_all_expenses() if e.category == category
    )
    if budget.is_over_budget(category, total_spent + amount):
        print(f"Warning: Adding this expense exceeds your budget for '{category}'!")

    expense = Expense(amount, category, description)
    if expense_service.save_expense(expense):
        print("Expense saved!")
    else:
        print("Failed to save expense.")


def list_expenses(expense_service):
    expenses = expense_service.get_all_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        print("\nExpenses:")
        for exp in expenses:
            print(f"- {exp}")


def set_budget_limit(budget):
    category = input("Enter category to set budget for: ").lower()
    amount = float(input(f"Enter budget limit for '{category}': "))
    budget.set_limit(category, amount)
    print(f"Budget set for category '{category}': ${amount:.2f}")


def view_budget_limits(budget):
    print("\nCurrent Budget Limits:")
    print(budget)


def delete_expense(expense_service):
    expense_id = input("Enter the ID of the expense to delete: ").strip()
    if expense_service.delete_expense(expense_id):
        print("Expense deleted successfully.")
    else:
        print("Expense ID not found.")


def update_expense(expense_service):
    expense_id = input("Enter the ID of the expense to update: ").strip()
    print("Enter new values (leave blank to keep current value): ")
    amount = input("New amount: ").strip()
    category = input("New category: ").strip().lower()
    description = input("New description: ").strip()

    new_data = {}
    if amount:
        new_data["amount"] = float(amount)
    if category:
        new_data["category"] = category
    if description:
        new_data["description"] = description

    if expense_service.update_expense(expense_id, new_data):
        print("Expense updated successfully.")
    else:
        print("Expense ID not found or no changes made.")


def report_with_dates(expense_service):
    start = (
        input("Enter start date (YYYY-MM-DD) or leave blank for no limit: ").strip()
        or None
    )
    end = (
        input("Enter end date (YYYY-MM-DD) or leave blank for no limit: ").strip()
        or None
    )
    generate_category_report(expense_service.load_all_expenses(), start, end)


def monthly_report(expense_service):
    year_input = input(
        "Enter year (YYYY) for monthly report or leave blank for all years: "
    ).strip()
    year = int(year_input) if year_input.isdigit() else None
    generate_monthly_report(expense_service.load_all_expenses(), year)


def weekly_report(expense_service):
    year_input = input(
        "Enter year (YYYY) for weekly report or leave blank for all years: "
    ).strip()
    year = int(year_input) if year_input.isdigit() else None
    generate_weekly_report(expense_service.load_all_expenses(), year)


def average_report(expense_service):
    generate_average_report(expense_service.load_all_expenses())


def category_pie_chart(expense_service):
    plot_category_pie_chart(expense_service.load_all_expenses())


def monthly_bar_chart(expense_service):
    year_input = input(
        "Enter year (YYYY) for monthly bar chart or leave blank for all years: "
    ).strip()
    year = int(year_input) if year_input.isdigit() else None
    plot_monthly_bar_chart(expense_service.load_all_expenses(), year)

def export_category_report_csv(expense_service):
    generate_category_report(expense_service.load_all_expenses(), export_csv=True)


def export_category_report_pdf(expense_service):
    # import here to avoid circular if export_report_to_pdf also imports report_service
    from services.export_service import export_report_to_pdf

    expenses = expense_service.load_all_expenses()
    df = export_to_csv_df = None
    if not expenses:
        print("No expenses found.")
        return
    from services.report_service import prepare_expense_dataframe  # Import helper

    df = prepare_expense_dataframe(expenses)
    category_totals = (
        df.groupby("category")["amount"].sum().sort_values(ascending=False).to_dict()
    )
    export_report_to_pdf(
        "Spending by Category Report", category_totals, "category_report.pdf"
    )


def exit_program():
    print("Goodbye!")
    exit()


def get_menu_choice(valid_choices):
    while True:
        choice = input("Enter choice: ").strip()
        if choice in valid_choices:
            return choice
        print(
            f"Invalid option '{choice}'. Please enter one of: {', '.join(valid_choices)}"
        )


def main():
    expense_service = ExpenseService()
    budget = Budget()

    options = {
        "1": lambda: add_expense(expense_service, budget),
        "2": lambda: list_expenses(expense_service),
        "3": lambda: set_budget_limit(budget),
        "4": lambda: view_budget_limits(budget),
        "5": lambda: update_expense(expense_service),
        "6": lambda: delete_expense(expense_service),
        "7": lambda: generate_category_report(expense_service.load_all_expenses()),
        "8": lambda: report_with_dates(expense_service),
        "9": lambda: monthly_report(expense_service),
        "10": lambda: weekly_report(expense_service),
        "11": lambda: average_report(expense_service),
        "12": lambda: category_pie_chart(expense_service),
        "13": lambda: monthly_bar_chart(expense_service),
        "14": lambda: export_category_report_csv(expense_service),
        "15": lambda: export_category_report_pdf(expense_service),
        "16": exit_program,
    }

    while True:
        print("\nChoose an option:")
        print("1. Add Expense")
        print("2. List All Expenses")
        print("3. Set Budget Limit for Category")
        print("4. View Budget Limits")
        print("5. Update an Expense")
        print("6. Delete an Expense")
        print("7. Show Spending by Category Report")
        print("8. Show Spending by Category Report (with date filter)")
        print("9. Show Monthly Spending Report")
        print("10. Show Weekly Spending Report")
        print("11. Show Average Spending by Category")
        print("12. Show Spending by Category Pie Chart")
        print("13. Show Monthly Spending Bar Chart")
        print("14. Export Category Report as CSV")
        print("15. Export Category Report as PDF")
        print("16. Exit")

        choice = get_menu_choice(options.keys())
        options[choice]()


if __name__ == "__main__":
    main()

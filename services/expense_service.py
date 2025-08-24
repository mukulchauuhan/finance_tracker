import json
import os
from typing import List, Dict
from models.expense import Expense

class ExpenseService:
    def __init__(self, data_file: str = "data/expenses.json"):
        self.data_file = data_file
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

    def save_expense(self, expense: Expense) -> bool:
        try:
            expenses = self.load_all_expenses()
            expenses.append(expense.to_dict())
            with open(self.data_file, 'w') as file:
                json.dump(expenses, file, indent=2)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def load_all_expenses(self) -> List[Dict]:
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_all_expenses(self) -> List[Expense]:
        expenses_dicts = self.load_all_expenses()
        return [Expense.from_dict(expense) for expense in expenses_dicts]

    def delete_expense(self, expense_id: str) -> bool:
        """Delete an expense by its unique ID"""
        expenses = self.load_all_expenses()
        new_expenses = [exp for exp in expenses if exp['id'] != expense_id]
        if len(new_expenses) == len(expenses): # No deletion happened
            return False
        with open(self.data_file, 'w') as file:
            json.dump(new_expenses, file, indent=2)
        return True

    def update_expense(self, expense_id: str, new_data: dict) -> bool:
        """
        Update fields for the expense with given id.
        new_data: dict with key like 'amount', 'category', 'description'.
        """
        expenses = self.load_all_expenses()
        updated = False
        for exp in expenses:
            if exp['id'] == expense_id:
                for key in new_data:
                    if key in exp:
                        exp[key] = new_data[key]
                updated = True
                break
        if not updated:
            return False
        with open(self.data_file, 'w') as file:
            json.dump(expenses, file, indent=2)
        return True


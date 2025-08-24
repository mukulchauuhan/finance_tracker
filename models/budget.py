# models/budget.py

class Budget:
    """
    Budget class models spending limits by category
    """

    def __init__(self):
        # Dictionary to hold category-wise budgets
        # key: category (str), value: limit amount (float)
        self.category_limits = {}

    def set_limit(self, category: str, amount: float) -> None:
        self.category_limits[category.lower()] = amount
    
    def get_limit(self, category: str) -> float:
        return self.category_limits.get(category.lower(), 0.0)
    
    def is_over_budget(self, category: str, spent: float) -> bool:
        limit = self.get_limit(category) # reusing get_limit method
        return spent > limit
    
    def __str__(self):
        """
        String representation to print current budget limits.
        """
        lines = []
        for cat, lim in self.category_limits.items():
            lines.append(f"{cat.title()}: ${lim:.2f}")

        return "\n".join(lines) if lines else "No budget limits set."
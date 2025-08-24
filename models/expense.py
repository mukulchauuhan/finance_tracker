from datetime import datetime
from typing import Optional


class Expense:
    def __init__(
        self,
        amount: float,
        category: str,
        description: str,
        date: Optional[datetime] = None,
    ):
        self.amount = amount
        self.category = category.lower()
        self.description = description
        self.date = date or datetime.now()
        self.id = self._generate_id()

    def _generate_id(self) -> str:
        return f"{self.date.strftime('%Y%m%d%H%M%S')}{hash(self.description) % 1000}"

    def to_dict(self) -> dict:
        # Converts the expense object to a dictionary
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=datetime.fromisoformat(data["date"]),
        )

    def __str__(self):
        return f"${self.amount:.2f} - {self.category} - {self.description} ({self.date.strftime('%Y-%m-%d')})"

class Expense:
    def __init__(self, amount, category, date, description=""):
        self.amount = float(amount)
        self.category = category
        self.date = date  # "YYYY-MM-DD"
        self.description = description

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["amount"], data["category"],
                   data["date"], data.get("description", ""))

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount:.2f} | {self.description}"
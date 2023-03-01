# class Transaction

class Transaction:

    def __init__(self, date: str, description: str, from_: str, to_: str, state: str, operation_amount: dict,
                 id: int = 0):
        self.id = id
        self.date: str = date
        self.description = description
        self.from_ = from_
        self.to_ = to_
        self.state = state
        self.operation_amount = operation_amount

    def __repr__(self):
        return f"Transaction({self.id}, {self.date}, {self.description}, {self.from_}, {self.to_}, {self.state}, {self.operation_amount})"

    def get_date_human_mode(self):
        return self.date[:10]

    def get_amount_human_mode(self):
        return self.operation_amount['amount']
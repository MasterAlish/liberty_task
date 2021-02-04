from decimal import Decimal


class Transaction:
    def __init__(self):
        self.created_date = None
        self.type = None
        self.amount = Decimal(0)
        self.source = None
        self.destination = None

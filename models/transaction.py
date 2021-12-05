from models import merchant


class Transaction:
    def __init__(self, amount, date, description, merchant=None, tag=None, id=None):
        self.amount = amount
        self.date = date
        self.description = description
        self.merchant = merchant
        self.tag = tag
        self.id = id

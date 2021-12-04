from models import merchant


class Transaction:
    def __init__(self, amount, date, description, merchant, tag, id=None):
        self.amount = amount
        self.date = date
        self.description = description
        self.merchant = merchant
        self.tag_id = tag
        self.id_id = id

class Transaction:
    
    def __init__(self, amount, date, description, id = None):
        self.amount = amount
        self.date = date
        self.description= description
        self.id = id
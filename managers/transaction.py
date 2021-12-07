import repositories.transaction_repository as transaction_repo

def total():
    total = 0
    transactions = transaction_repo.select_all()
    for x in transactions:
        total += x.amount
    return total

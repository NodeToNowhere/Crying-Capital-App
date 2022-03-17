from datetime import datetime
import repositories.transaction_repository as transaction_repo


def total():
    total = 0
    transactions = transaction_repo.select_all()
    for x in transactions:
        total += x.amount
    return total


def get_dates():
    unsorted_dates = []
    dates = []
    format_data = "%d-%m-%y"
    transactions = transaction_repo.select_all()
    [unsorted_dates.append(transaction.date) for transaction in transactions]
    [dates.append(datetime.strptime(date, format_data)) for date in unsorted_dates]
    [print(date.day, date.month, date.year) for date in dates]
    return dates

    
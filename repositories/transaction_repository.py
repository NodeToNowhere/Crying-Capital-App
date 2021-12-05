from db.run_sql import run_sql
from models.transaction import Transaction


#Todo - Write update_transaction for merchant and tag that links tables that can take null/empty


# ---Create


def save(transaction):
    sql = "INSERT INTO transactions(amount, date, description, merchant_id,tag_id) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [
        transaction.amount,
        transaction.date,
        transaction.description,
        transaction.merchant.id,
        transaction.tag.id,
    ]
    results = run_sql(sql, values)
    transaction.id = results[0]["id"]
    return transaction


# ---Read


def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        transaction = Transaction(result["transaction"])
    return transaction


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        transaction = transaction(row["amount"], row["date"], row["description"])
        transactions.append(transaction)
    return transactions


# ---Update


def update(transaction):
    sql = "UPDATE transactions SET (amount,date,description,merchant_id,tag_id) = (%s,%s,%s,%s,%s) WHERE id = %s"
    values = [
        transaction.amount,
        transaction.date,
        transaction.description,
        transaction.merchant.id,
        transaction.tag.id,
        transaction.id,
    ]
    run_sql(sql, values)


# --Delete


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

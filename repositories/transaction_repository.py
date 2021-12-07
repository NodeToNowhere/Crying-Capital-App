from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo


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
        merchant = merchant_repo.select(row["merchant_id"])
        tag = tag_repo.select(row["tag_id"])
        transaction = Transaction(
            row["amount"], row["date"], row["description"], merchant, tag, row["id"]
        )
        transactions.append(transaction)
    return transactions


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


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def set_default():
#     sql_default_m = "ALTER TABLE ONLY transactions ALTER COLUMN merchant_id SET DEFAULT ''"
#     sql_update_m = "UPDATE transactions SET merchant_id = '' WHERE lang IS NULL"
#     sql_default_t = "ALTER TABLE ONLY transactions ALTER COLUMN tag_id SET DEFAULT ''"
#     sql_update_t = "UPDATE transactions SET tag_id = '' WHERE lang IS NULL"
    
#     run_sql(sql_default_m)
#     run_sql(sql_update_m)
#     run_sql(sql_default_t)
#     run_sql(sql_update_t)
    
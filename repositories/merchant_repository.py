from db.run_sql import run_sql
from models.merchant import Merchant


# ---Create


def save(merchant):
    sql = "INSERT INTO merchants(merchant) VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]["id"]
    return merchant


# ---Read


def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result["merchant"])
    return merchant


# ---Update

# --Delete

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

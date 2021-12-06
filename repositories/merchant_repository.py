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
        merchant = Merchant(result["merchant"],result['id'])
    return merchant


def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row["merchant"],row['id'])
        merchants.append(merchant)
    return merchants


# ---Update

def update(merchant):
    sql= "UPDATE merchants SET (name) = (%s) WHERE id = %s"
    values = [merchant.name,merchant.id]
    run_sql(sql,values)

# --Delete


def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

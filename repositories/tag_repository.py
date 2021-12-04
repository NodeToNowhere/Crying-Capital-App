from db.run_sql import run_sql
from models.tag import Tag


# ---Create


def save(tag):
    sql = "INSERT INTO tags(tag) VALUES (%s) RETURNING id"
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id = results[0]["id"]
    return tag


# ---Read


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result["tag"])
    return tag


def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = tag(row["tag"])
        tags.append(tag)
    return tags


# ---Update

def update(tag):
    sql= "UPDATE tags SET (name) = (%s) WHERE id = %s"
    values = [tag.name,tag.id]
    run_sql(sql,values)

# --Delete


def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

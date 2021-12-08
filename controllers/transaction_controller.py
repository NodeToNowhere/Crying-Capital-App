from flask import Flask, render_template, request, redirect, Blueprint
from models.transaction import Transaction
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo
from managers.transaction import *

transaction_blueprint = Blueprint("transaction", __name__)


@transaction_blueprint.route("/")
def home():
    return redirect("/transactions")


@transaction_blueprint.route("/transactions")
def transactions():
    tags = tag_repo.select_all()
    merchants = merchant_repo.select_all()
    transactions = transaction_repo.select_all()
    return render_template(
        "transactions/overview.html",
        transactions=transactions,
        tags=tags,
        merchants=merchants,
        total=total(),
    )


@transaction_blueprint.route("/transactions/new", methods=["POST"])
def new_transaction():
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    merchant = merchant_repo.select(merchant_id)
    tag = tag_repo.select(tag_id)
    amount = request.form["amount"]
    date = request.form["date"]
    description = request.form["description"]
    transaction = Transaction(amount, date, description, merchant, tag)
    transaction_repo.save(transaction)
    return redirect("/transactions")


@transaction_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repo.delete(id)
    return redirect("/transactions")

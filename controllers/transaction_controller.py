from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo

transaction_blueprint = Blueprint("transaction", __name__)


@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repo.select_all()
    return render_template("/transactions/show.html", transactions=transactions)


@transaction_blueprint.route("/transactions/new", methods=["POST"])
def new_transaction():
    new_transaction = Transaction(
        request.form["amount"],
        request.form["date"],
        request.form["description"],
        request.form["merchant"],
        request.form["tag"],
    )
    transaction_repo.save(new_transaction)
    return redirect("/transactions")

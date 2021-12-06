from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.transaction_repository as transaction_repo

transaction_blueprint = Blueprint("transaction", __name__)


@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repo.select_all()
    return render_template("/transactions/transactions.html", transactions=transactions)

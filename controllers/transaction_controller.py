from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo

transaction_blueprint = Blueprint("transaction", __name__)


@transaction_blueprint.route("/transaction")
def transaction():
    return render_template(
        "/transactions/transaction.html", test="this is transaction test"
    )

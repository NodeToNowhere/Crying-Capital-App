from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.merchant_repository as merchant_repo


merchant_blueprint = Blueprint("merchants", __name__)


@merchant_blueprint.route("/labels/new/merchant", methods=["POST"])
def new_merchant():
    new_merchant = Merchant(request.form["merchant_name"])
    merchant_repo.save(new_merchant)
    return redirect("/labels")


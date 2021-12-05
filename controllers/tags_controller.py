from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as mer_repo
from models.merchant import Merchant
from models.tag import Tag

tags_bp = Blueprint("tags", __name__)


# GET
@tags_bp.route("/labels", methods=["GET"])
def labels():
    tags = tag_repo.select_all()
    merchants = mer_repo.select_all()
    return render_template("labels/labels.html", tags=tags, merchants=merchants)


# POST
@tags_bp.route("/labels/new", methods=["POST"])
def new_label():
    new_tag = Tag(request.form["tag"])
    tag_repo.save(new_tag)
    new_merchant = Merchant(request.form["merchant"])
    mer_repo.save(new_merchant)
    return redirect("/labels")  # show confirmation or goto labels?


# DELETE
@tags_bp.route("/labels/delete/<id>", methods=["POST"])
def delete_label(id):
    tag_repo.delete(id)
    mer_repo.delete(id)
    return redirect("/labels")


# add an edit function later

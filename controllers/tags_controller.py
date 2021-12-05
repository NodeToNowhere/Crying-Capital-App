from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as mer_repo
from models.merchant import Merchant
from models.tag import Tag

tags_bp = Blueprint("tags", __name__)


@tags_bp.route("/new_label")
def new_label():
    new_tag = Tag(request.form["tag"])
    tag_repo.save(new_tag)
    new_merchant = Merchant(request.form["merchant"])
    mer_repo.save(new_merchant)
    return render_template("/new_label")  # show confirmation

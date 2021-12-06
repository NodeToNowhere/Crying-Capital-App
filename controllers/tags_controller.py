from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo

tags_blueprint = Blueprint("transactions", __name__)


@tags_blueprint.route("/tags")
def tags():
    tags = tag_repo.select_all()
    return render_template("tags/tags.html", tags=tags)


# POST
# show confirmation or goto tags?
# split into tag and merchant (new)


@tags_blueprint.route("/tags/new", methods=["POST"])
def new_tag():
    new_tag = Tag(request.form["tag_name"])
    tag_repo.save(new_tag)
    return redirect("/tags")


# DELETE
@tags_blueprint.route("/tags/delete/<id>", methods=["POST"])
def delete_label(id):
    tag_repo.delete(id)
    merchant_repo.delete(id)
    return redirect("/tags")


# add an edit function later

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as mer_repo

trans_bp = Blueprint("transactions", __name__)

@trans_bp.route('/')
def index():
    return render_template('index.html')


    

    
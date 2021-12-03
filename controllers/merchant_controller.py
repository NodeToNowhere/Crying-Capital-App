from flask import Flask, render_template, request, redirect
from flask import Blueprint


merchant_blueprint = Blueprint("merchants", __name__)

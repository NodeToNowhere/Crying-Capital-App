from flask import Flask, render_template, request, redirect
from flask import Blueprint

tags_blueprint = Blueprint("tags", __name__)

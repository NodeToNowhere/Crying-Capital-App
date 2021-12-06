from flask import Flask, render_template
from controllers.merchant_controller import merchant_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.transaction_controller import transaction_blueprint

app = Flask(__name__)

app.register_blueprint(merchant_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(transaction_blueprint)


@app.route("/")
def home():
    return render_template("index.html", test="THIS IS A TEST")


if __name__ == "__main__":
    app.run(debug=True)

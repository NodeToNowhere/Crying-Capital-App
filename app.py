from flask import Flask, render_template
from controllers.merchant_controller import merchant_blueprint
from controllers.tags_controller import tags_blueprint
from controllers.transaction_controller import transaction_blueprint
import logging

app = Flask(__name__)


logging.basicConfig(
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


app.register_blueprint(merchant_blueprint)
app.register_blueprint(tags_blueprint)
app.register_blueprint(transaction_blueprint)


if __name__ == "__main__":
    app.run(debug=True)

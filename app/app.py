from flask import Flask,url_for
from app.api.v1 import bp_v1
app = Flask(__name__)
app.config.from_object('app.etc.conf')

app.register_blueprint(bp_v1,url_prefix='/v1')

@app.route('/')
def index():
    return url_for("v1.get")


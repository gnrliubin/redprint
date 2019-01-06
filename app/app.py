from flask import Flask
from app.api import v1
app = Flask(__name__)
app.config.from_object('app.etc.conf')

app.register_blueprint(v1.bp_v1,url_prefix='/v1')

@app.route('/')
def index():
    return "index"




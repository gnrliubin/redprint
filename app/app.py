"""
Flask实例，并把蓝图注册到实例，导入配置文件
"""
from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
from app.api.v1 import bp_v1
app = Flask(__name__)
app.config.from_object('app.etc.conf')
app.config.from_object('app.etc.secret')

app.register_blueprint(bp_v1,url_prefix='/v1')

# db = SQLAlchemy(app)

@app.route('/')
def index():
    return url_for("v1.get")


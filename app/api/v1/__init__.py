from flask import Blueprint

'''
bp_v1 = Blueprint('v1',__name__,url_prefix='/v1')
blueprint.py 50~55 ,options中的url_prefix会覆盖这里的url_prefix
options参数来自于app.register_blueprint
'''
bp_v1 = Blueprint('v1',__name__)

#from . import *     # 这样导入会找不到路由，一定要用下面方式导入
from . import user,token
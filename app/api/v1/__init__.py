from flask import Blueprint


bp_v1 = Blueprint('v1',__name__)

#from . import *     # 这样导入会找不到路由，一定要用下面方式导入
from . import user,token

from app.libs.redprint import RedPrint

api = RedPrint('token')

@api.route("/get")
def get():
    return __name__


@api.route('/post')
def post():
    return "v1-token-post"

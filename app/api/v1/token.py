
from app.libs.redprint import RedPrint

api = RedPrint('token')

@api.route("/get")
def get():
    return "v1-token-get11"


@api.route('/post')
def post():
    return "v1-token-post"

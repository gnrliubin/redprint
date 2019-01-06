from . import bp_v1

@bp_v1.route("/token/get")
def get():
    return "v1-token-get"


@bp_v1.route('/token/post')
def post():
    return "v1-token-post"

from . import bp_v1

@bp_v1.route('/user/get',endpoint='getuser')
def get():
    return "v1-user-get"

@bp_v1.route('/user/post',endpoint='postuser')
def post():
    return "v1-user-post"
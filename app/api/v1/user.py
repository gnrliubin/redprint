
from app.libs.redprint import RedPrint

api = RedPrint('user')

@api.route('/get')
def get_user():
    return "v1-user-get"

@api.route('/post')
def change_user():
    return "v1-user-post"
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, request


# All views that only admins are allowed to see should inherit from this class
class AuthVeiw(ModelView):

    def is_accessible(self):
        return True
        # TODO: import login
        # return login.current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))  

class UserView(AuthVeiw):
    column_list = ('username', 'email', 'role', 'isActive', 'course')
    column_filters = ('isActive', 'role')
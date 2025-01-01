from flask_admin import AdminIndexView
from flask_admin import expose
from flask_login import login_required


class IndexView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        return super().index()

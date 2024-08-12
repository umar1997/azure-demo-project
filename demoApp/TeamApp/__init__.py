import os
from TeamApp.models import app, db
from TeamApp.models import User

STATIC_URL = '/static/'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# db.init_app(app)

with app.app_context():
    db.create_all()

####################################### Blueprint

from TeamApp.core.views import core_
from TeamApp.member.views import member_
from TeamApp.team.views import team_
from TeamApp.error_pages.handlers import error_pages_

app.register_blueprint(core_)
app.register_blueprint(member_)
app.register_blueprint(team_)
app.register_blueprint(error_pages_)
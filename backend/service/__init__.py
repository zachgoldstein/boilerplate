from flask import Flask

from service.main.controllers import main
from service.admin.controllers import admin
from common import tracing

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

with app.app_context():
    tracing.get_tracer(app)

@app.teardown_appcontext
def teardown_tracer(exception):
    tracing.teardown_tracer(exception)

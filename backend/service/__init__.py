from flask import Flask
from flask import g
from service.main.controllers import main
from service.admin.controllers import admin
import opentracing
from flask_opentracing import FlaskTracer
import logging
import time
from jaeger_client import Config

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

def setup_tracer():
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name='boilerplate-service',
    )
    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()

FlaskTracer(setup_tracer(), True, app, ["boilerplate-service"])

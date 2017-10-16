import time

import opentracing
from flask_opentracing import FlaskTracer

tracer = None

def get_tracer(app):
    global tracer
    if tracer is None:
        tracer = FlaskTracer(
            opentracing.tracer, True, app, ["boilerplate-service"]
        )
    return tracer

def teardown_tracer(exception):
    if tracer is not None:
        # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
        time.sleep(2)
        opentracing.tracer.close()

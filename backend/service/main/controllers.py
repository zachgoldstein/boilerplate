from flask import Blueprint, current_app
import time
import random
from common import tracing

main = Blueprint('main', __name__)

def test_sleeper():
    time.sleep(random.uniform(0, 1))

@main.route('/')
def index():
    test_sleeper()
    # import pdb; pdb.set_trace()
    tracer = tracing.get_tracer(current_app)
    span = tracer.get_span()
    span.log_event("hello world")
    # parent_span = tracer.get_span()
    parent_span = tracer.get_span()
    span = tracer._tracer.start_span("baby span", child_of=parent_span)
    time.sleep(random.uniform(0, 1))
    span.finish()
    return "Main"

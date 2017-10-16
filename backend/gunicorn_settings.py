import opentracing
import logging
import time
from jaeger_client import Config

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

def post_fork(server, worker):
    setup_tracer()

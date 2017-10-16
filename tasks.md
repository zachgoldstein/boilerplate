# Tasks:

### Backend:
DONE Figure out why opentracing crashes flask app:
  https://github.com/jaegertracing/jaeger-client-python/issues/60
  variety of challenges here:
    - Needed to make sure it was created with app context:
    with app.app_context():
        tracing.get_tracer(app)
    - Needed to make sure we were not initialising the tracer twice

Make sure tracing across the wire is correlated correctly

Add logging
Add auth
Add statsd
Add emailer
Add async tasks


### Frontend:
add material-UI components
add chart components
add form components

### Common:
Figure out workflow for openapi spec file .OAS to generate frontend service and backend models

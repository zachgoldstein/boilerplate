boiler plate notes

# Goals:

- Single source of truth for models, sync everywhere quickly
- Built-in measurement tools
  - Performance across entire stack (open tracing, statsd)
  - User analytics across entire stack (mixpanel)
  -
- Easy ad-hoc analysis (Models/DB access built-in to notebook)
- Quick out-of-band task dev (via celery etc)
- Quick deploys (Heroku first, then AWS)
- Quick mocked backend from swagger for easy UI dev.
- Cheap to run
- Easy to scale
- CI/CD notes work
-

## What Usually Goes Wrong:

- Models get out of sync and SOC violations explode
- Duplication runs wild
- Frontend state management becomes a nightmare
- Backend deploy process takes too long
- No tracking of errors/logs
- Deployment is not quick
- Security stuff mires development (auth/CSRF/CORS)
- Out-of-band tasks are not easy to setup
- Ad-hoc analysis is a pain
- Frontend dev gets hung up on backend trivialities
- Alerting on stats, not time it takes to fix

## Infra:

### Frontend

DONE reactjs
redux
axois
DONE http://www.material-ui.com/
https://redux-form.com/7.0.4/examples/material-ui/
https://github.com/uber/react-vis
http://flexboxgrid.com/
redux-thunk
redux-saga

colors: https://www.materialpalette.com/
icons: https://design.google.com/icons/
time conveniences: https://momentjs.com/


### Backend

Goals:
  - generate from OAS
  - strong model/db tools. migrations, refs, etc
  - tracing
  - throttling
  - logging
  - async tasks & queuing setup
  - easy emailer
  - auth setup

djangorest is hard to generate from an OAS file.
flask is going to be tricky to glue things together

DjangoREST: http://www.django-rest-framework.org/
Flask
  - migrations: http://alembic.zzzcomputing.com/en/latest/tutorial.html



ORM via postgres
good built-in auth (CSRF, CORS, XSS)
statsd: http://django-statsd.readthedocs.io/en/latest/index.html
opentracing: https://github.com/opentracing-contrib/python-django
Celery Queues
mandrill
throttling
good logging

### PROD Tools

Metrics via Statsd and grafana
Opentracing via jaeger
Mixpanel integration (analytics)
Logging service


### DEV Tools

Mocking via https://stoplight.io/platform/prism/
Juypter Notebook (using django-extensions)
After effects to JS -> https://github.com/bodymovin/bodymovin

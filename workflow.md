# Workflow notes:


Schema syncing process
- generate OAS file from a few places
  - export from stoplight
  - OR generate from djangoREST
- build service layer from coreAPI description (https://github.com/mikestead/openapi-client)

To modify models in the system:
  - Modify schema via stoplight
  - Build backend API off description
  - Generate frontend API service

General dev process:
- Start with the UI and a mocked backend
  - https://stoplight.io/platform/prism/
- Generate frontend API service
-




## Using stoplight, pros/cons:

### pros
quick to setup models, fields.
generating the example data from the schema is nice

### cons
kind of janky to go from API -> mock request
  have to remember to generate the example object
feels naughty to use a UI-based tool like this

Boilerplate Setup Notes:

Installing Prism (Mock Server):

curl https://raw.githubusercontent.com/stoplightio/prism/master/install.sh | sh

Stoplight! http://stoplight.io/platform/design/


Running react-app
npm start

Starting Jaeger
docker run -d -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp -p5778:5778 -p16686:16686 -p14268:14268 -p9411:9411 jaegertracing/all-in-one:latest

Mock out state shape via dummy data in actions.js:
```
.then(dispatch(receivePosts(subreddit, dummyData)))
// .then(json => dispatch(receivePosts(subreddit, json)))
```

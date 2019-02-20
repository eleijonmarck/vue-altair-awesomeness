# vue-altair-awesomeness
Trying out the new technology of Vue and Altair

```
npm install -g vue-cli
```

Then you can use `vue` to instantiate a new application template. We use the
more complicated webpack example here as we want to have a running webpack
server.

```
vue init webpack altair-awesomeness
```

 * In `build/webpack.dev.conf.js`, we have added `disableHostCheck: true` so that
   in development the server is accesible from any hosts. This allows port
   forwarding to other hosts, e.g. when running from a container.
 * In `config/index.js` add an entry that will forward to our local Flask app
   where we will generate the Vega spec using Altair.
   ```
   proxyTable: {
     '/vega-example': 'http://localhost:5000'
   },
   ```
 * Install `vega-embed` using 
 
```
npm install --save vega-embed
```
 * In `HelloWorld.vue`, we have added a script section that will call our Flask
   backend that returns the Vega specification using Altair.

## Running

Flask backend
```bash
$ FLASK_APP=app.py flask run
```

```bash
$ cd altair-awesomeness
$ npm run dev
``` 

### Inspired by:

https://github.com/xhochy/altair-vue-vega-example


https://www.youtube.com/watch?v=4L568emKOvs

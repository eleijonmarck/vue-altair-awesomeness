<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadImage()">Fuel Flow</v-btn>
        <div id="vega-example-box"></div>
      </v-layout>
    </v-slide-y-transition>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadAltitude()">Altitude</v-btn>
        <div id="vega-altitude"></div>
      </v-layout>
    </v-slide-y-transition>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadLatLong()">Lat/Long</v-btn>
        <div id="vega-latlong"></div>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import {default as vegaEmbed} from 'vega-embed'
export default {
  methods: {
    reloadImage () {
      fetch('/vega-example').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-example-box', spec, {actions: false})
        })
      })
    },
    reloadAltitude () {
      fetch('/vega-altitude').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-altitude', spec, {actions: false})
        })
      })
    },
    reloadLatLong () {
      fetch('/vega-latlong').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-latlong', spec, {actions: false})
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

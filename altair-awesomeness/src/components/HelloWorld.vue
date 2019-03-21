<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadExample1()">Example One</v-btn>
        <div id="vega-example1"></div>
      </v-layout>
    </v-slide-y-transition>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadExample2()">Example two</v-btn>
        <div id="vega-example2"></div>
      </v-layout>
    </v-slide-y-transition>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadExample3()">Example three</v-btn>
        <div id="vega-example3"></div>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import {default as vegaEmbed} from 'vega-embed'
export default {
  methods: {
    reloadImage () {
      fetch('/vega-example1').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-example', spec, {actions: false})
        })
      })
    },
    reloadAltitude () {
      fetch('/vega-example2').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-example2', spec, {actions: false})
        })
      })
    },
    reloadLatLong () {
      fetch('/vega-example3').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-example3', spec, {actions: false})
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

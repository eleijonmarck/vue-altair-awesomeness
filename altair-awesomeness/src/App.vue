<template>
  <v-app>
    <v-content>
      <router-view/>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [{
        icon: 'bubble_chart',
        title: 'Altair, Vega and Vue'
      }],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'PyData Amsterdam Demo'
    }
  },
  name: 'App'
}
</script>

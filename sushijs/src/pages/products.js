import Vue from 'vue'
import Products from './Products.vue'
import store from '../store'
import '../plugins/axios'

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(Products),
}).$mount('#products')

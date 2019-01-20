import Vue from 'vue'
import Products from './Products.vue'
import store from '../store'
import '../plugins/axios'
import {app} from '../main'

Vue.config.productionTip = false

console.dir()

new Vue({
  store,
  render: h => h(Products),
}).$mount('#products')

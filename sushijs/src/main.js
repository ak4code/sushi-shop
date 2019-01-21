import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import Products from './pages/Products.vue'
import Checkout from './pages/Checkout.vue'
import store from './store'
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons';
import './styles/app.scss'

Vue.config.productionTip = false

UIkit.use(Icons);

const cartApp = new Vue({
  store,
  render: h => h(App),
}).$mount('#app')

const products = new Vue({
  store,
  render: h => h(Products),
})

const checkout = new Vue({
  store,
  render: h => h(Checkout),
})

if (document.getElementById('products')) {
  products.$mount('#products')
}

if (document.getElementById('checkout')) {
  checkout.$mount('#checkout')
}

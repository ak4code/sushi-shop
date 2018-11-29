import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import store from './store'
import UIkit from 'uikit/dist/js/uikit-core.min'
import './styles/app.scss'

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')

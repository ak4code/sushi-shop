import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import store from './store'
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons';
import './styles/app.scss'

Vue.config.productionTip = false

UIkit.use(Icons);

const app = new Vue({
  store,
  render: h => h(App),
}).$mount('#app')

export default {
  app
}

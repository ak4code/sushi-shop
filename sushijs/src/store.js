import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    basket: {}
  },
  getters: {
    cart: state => {
      return state.basket
    }
  },
  mutations: {
    SET_CART(state, data) {
      state.basket = data
    }
  },
  actions: {
    async initCart({commit}) {
      let {data} = await axios.post('/api/carts/init/')
      commit('SET_CART', data)
    },
    async addToCart({state, dispatch}, item) {
      console.log(item)
      let {data} = await axios.post('/api/cart-items/', item)
      await dispatch('initCart')
    }
  },
});

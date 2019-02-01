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
    },
    checkProductInCart: (state) => (id) => {
      return Boolean(state.basket.items.find(item => item.product === id))
    }
  },
  mutations: {
    SET_CART (state, data) {
      state.basket = data
    }
  },
  actions: {
    async initCart ({commit}) {
      let {data} = await axios.post('/api/carts/init/')
      commit('SET_CART', data)
    },
    async addToCart ({state, dispatch}, productId) {
      let {data} = await axios.post('/api/cart-items/', {product: productId, cart: state.basket.id, quantity: 1})
      await dispatch('initCart')
    },
    async updateItemCart ({dispatch}, item) {
      let {data} = await axios.patch(`/api/cart-items/${item.id}/`, item)
      await dispatch('initCart')
    },
    async deleteItemCart ({dispatch}, item) {
      let {data} = await axios.delete(`/api/cart-items/${item.id}/`)
      await dispatch('initCart')
    },
    async checkout ({dispatch}, order) {
      let {data} = await axios.post('/api/orders/', order)
      return data
    }
  },
});

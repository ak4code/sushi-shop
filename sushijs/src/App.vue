<template>
  <div id="cart">
    <div class="uk-flex uk-flex-center uk-flex-wrap uk-grid-small">
      <a href="/cart" class="cart-btn">
        <div><span uk-icon="icon: cart; ratio: 1"></span> Корзина: <strong>0 руб.</strong></div>
        {{cart.id}}
      </a>
    </div>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    name: 'app',
    created() {
      this.initCart()
    },
    computed: {
      ...mapGetters({
        cart: 'cart'
      })
    },
    methods: {
      ...mapActions({
        initCart: 'initCart'
      })
    }
  }
</script>

<style>
</style>

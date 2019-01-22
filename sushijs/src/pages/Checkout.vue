<template>
  <div id="checkout">
    <div class="uk-flex uk-flex-wrap uk-grid-small" v-if="!order.send">
      <div class="uk-width-3-4@m">
        <div class="uk-overflow-auto">
          <table class="uk-table uk-table-hover uk-table-middle uk-table-divider">
            <thead>
            <tr>
              <th class="uk-table-shrink"></th>
              <th class="uk-table-expand">Продукт</th>
              <th class="uk-table-shrink uk-text-nowrap">Цена</th>
              <th class="uk-width-small">Кол-во</th>
              <th class="uk-table-shrink uk-text-nowrap">Сумма</th>
              <th class="uk-table-shrink"></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in cart.items" :key="item.id">
              <td><img class="uk-preserve-width uk-border-rounded" :src="item.productInfo.image" width="40" alt=""></td>
              <td>
                {{item.productInfo.title}}
              </td>
              <td class="uk-text-nowrap">
                {{item.productInfo.price}}
              </td>
              <td>
                <input class="uk-input uk-form-small" type="number" min="1" :value="item.quantity"
                       @change="changeQuantity(item, $event)">
              </td>
              <td class="uk-text-nowrap">
                {{item.amount}} руб.
              </td>
              <td>
                <a class="uk-preserve-width" uk-icon="icon: trash" @click="deleteItem(item)"></a>
              </td>
            </tr>
            </tbody>
            <tfoot>
            <tr>
              <td colspan="6" class="uk-text-right">
                <strong>Итого: {{cart.total}} руб.</strong>
              </td>
            </tr>
            </tfoot>
          </table>
        </div>
      </div>
      <div class="uk-width-1-4@m">
        <div class="uk-card uk-card-default uk-card-small uk-card-body">
          <form class="uk-form-stacked" v-on:submit.prevent="sendOrder">
            <div class="uk-margin">
              <label class="uk-form-label" for="client-name">Как Вас зовут?</label>
              <div class="uk-form-controls">
                <input class="uk-input" required v-model="order.name" id="client-name" type="text" placeholder="Имя">
              </div>
            </div>
            <div class="uk-margin">
              <label class="uk-form-label" for="client-phone">Номер телефона</label>
              <div class="uk-form-controls">
                <input class="uk-input" required v-model="order.phone" id="client-phone" type="text"
                       placeholder="+7 (999) 999-99-99">
              </div>
            </div>
            <div class="uk-margin">
              <label class="uk-form-label" for="client-address">Адрес</label>
              <div class="uk-form-controls">
                <input class="uk-input" required v-model="order.address" id="client-address" type="text"
                       placeholder="Темрюк, ул. Таманская 6">
              </div>
            </div>
            <div class="uk-margin">
              <label class="uk-form-label" for="client-person">Количество персон</label>
              <div class="uk-form-controls">
                <select class="uk-select" id="client-person" v-model="order.person">
                  <option v-for="n in 10" :key="n">{{n}}</option>
                </select>
              </div>
            </div>
            <div class="uk-margin">
              <div class="uk-form-controls">
                <button class="uk-button uk-button-primary uk-width-1-1"
                        :disabled="cart.items.length ? false : true">
                  ОФОРМИТЬ ЗАКАЗ
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="uk-flex uk-flex-center uk-flex-wrap uk-grid-small" v-if="order.send">
      <div class="uk-text-center">
        <div class="uk-padding-large uk-margin-large">
          <span uk-icon="icon: happy; ratio: 6" class="uk-margin" style="color: lawngreen"></span>
          <h1>ЗАКАЗ ОФОРМЛЕН</h1>
          <p class="uk-text-lead">Наш менеджер свяжется с Вами для уточнения и подтверждения заказа в ближайшее время.</p>
          <a href="/">Вернуться на главную</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: "checkout",
    data: () => ({
      order: {
        name: '',
        phone: '',
        address: '',
        person: 1,
        send: false
      }
    }),
    computed: {
      ...mapGetters({
        cart: 'cart'
      })
    },
    methods: {
      changeQuantity (item, $event) {
        this.updateItemCart({id: item.id, quantity: $event.target.valueAsNumber})
      },
      deleteItem (item) {
        this.deleteItemCart(item)
      },
      sendOrder () {
        this.order.cart = this.cart.id
        this.checkout(this.order)
          .then(data => this.order = data)
      },
      ...mapActions({
        updateItemCart: 'updateItemCart',
        deleteItemCart: 'deleteItemCart',
        checkout: 'checkout',
      })
    }
  }
</script>

<style scoped>

</style>

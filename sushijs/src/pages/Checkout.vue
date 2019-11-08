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
        <div class="uk-margin">
          <div class="uk-overflow-auto">
            <table class="uk-table uk-table-condensed" style="color: #000;" border="3" cellpadding="7" bgcolor="white">
              <thead>
              <tr>
                <th class="uk-width-1-3 uk-text-center" style="background-color: red; color: #fff;">Доставка</th>
                <th class="uk-width-1-3 uk-text-center" style="background-color: red; color: #fff;">до 500 р.</th>
                <th class="uk-width-1-3 uk-text-center" style="background-color: red; color: #fff;">от 500 р.</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td class="uk-width-1-3 uk-text-center">Темрюк</td>
                <td class="uk-width-1-3 uk-text-center">100 р.</td>
                <td class="uk-width-1-3 uk-text-center">бесплатно</td>
              </tr>
              <tr>
                <td class="uk-width-1-3 uk-text-center">ст. Голубицкая
                </td>
                <td class="uk-width-1-3 uk-text-center">200 р.</td>
                <td class="uk-width-1-3 uk-text-center">100 р.</td>
              </tr>
              <tr>
                <td class="uk-width-1-3 uk-text-center">ст. Курчанская
                </td>
                <td class="uk-width-1-3 uk-text-center">300 р.</td>
                <td class="uk-width-1-3 uk-text-center">200 р.</td>
              </tr>
              <tr>
                <td class="uk-width-1-3 uk-text-center">п. Октябрьский
                </td>
                <td class="uk-width-1-3 uk-text-center">250 р.</td>
                <td class="uk-width-1-3 uk-text-center">150 р.</td>
              </tr>
              </tbody>
            </table>
          </div>
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
            <div class="uk-margin uk-grid-small uk-child-width-auto uk-grid">
              <label><input class="uk-radio" type="radio" :value="true" v-model="order.delivery" name="delivery">Доставка</label>
              <label><input class="uk-radio" type="radio" :value="false" v-model="order.delivery" name="delivery">Самовывоз</label>
            </div>
            <div class="uk-margin" v-if="order.delivery">
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
              <div class="uk-form-controls" v-if="cart.items">
                <button class="uk-button uk-button-primary uk-width-1-1"
                        :disabled="cart.items.length ? false : true">
                  ОФОРМИТЬ ЗАКАЗ
                </button>
              </div>
            </div>
            <div class="uk-margin uk-text-small uk-text-muted">
              Нажимая кнопку «Оформить заказ», я подтверждаю свою дееспособность,
              согласие на обработку персональных
              данных в соответствии с указанным <a href="/policy/" target="_blank">здесь</a> текстом.
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
          <p class="uk-text-lead">Ожидайте звонка оператора для потверждения заказа.</p>
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
        send: false,
        delivery: true,
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
        if (!this.order.delivery) {
          this.order.address = 'САМОВЫВОЗ'
        }
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

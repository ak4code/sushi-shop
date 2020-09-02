<template>
  <div id="checkout">
    <div class="uk-flex uk-flex-wrap uk-grid-small" v-if="!order.send">
      <div class="uk-width-3-4@m">
        <div class="cart-item-list">
          <div class="cart-item uk-flex uk-flex-wrap uk-flex-middle uk-grid-small"
               v-for="(item, index) in cart.items" :key="index">
            <div class="item-image uk-width-auto">
              <div class="uk-cover-container">
                <canvas width="100" height="100"></canvas>
                <img :src="item.productInfo.image" :alt="item.productInfo.title" width="100"
                     height="100" uk-cover>
              </div>

            </div>
            <div class="item-info uk-width-expand">
              <div class="uk-flex uk-flex-wrap uk-flex-middle uk-grid-small">
                <div class="uk-width-expand">
                  <h5 class="uk-margin-small-bottom">{{item.productInfo.title}}</h5>
                </div>
                <div class="uk-width-1-5@m uk-text-center">
                  <input class="uk-input" min="1" max="999" type="number" :value="item.quantity"
                         @change="changeQuantity(item, $event)">
                  <small>{{item.productInfo.price}} ₽ / шт.</small>
                </div>
                <div class="uk-width-1-5@m uk-flex-first uk-flex-last@m">
                  <div class="uk-text-large uk-text-bold">
                    {{item.amount}} ₽
                  </div>
                </div>
              </div>
            </div>
            <div class="uk-width-auto uk-padding-small">
              <a @click="deleteItem(item)" uk-icon="trash"></a>
            </div>
          </div>
        </div>
        <div class="uk-padding uk-text-right">
          <h4 class="uk-margin-remove uk-text-bold">Итого: {{cart.total}} ₽ *</h4>
          <small class="uk-text-muted">* Без учета стоимости доставки</small>
        </div>
        <div class="uk-margin">
          <div class="uk-overflow-auto" v-html="page.content"></div>
        </div>
      </div>
      <div class="uk-width-1-4@m">
        <div class="uk-card uk-card-default uk-card-small uk-card-body">
          <form class="uk-form-stacked" v-on:submit.prevent="sendOrder">
            <div class="uk-margin">
              <label class="uk-form-label" for="client-name">Как Вас зовут?</label>
              <div class="uk-form-controls">
                <input class="uk-input" required v-model="order.name" id="client-name" type="text"
                       placeholder="Имя">
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
              <label><input class="uk-radio" type="radio" :value="true" v-model="order.delivery"
                            name="delivery">Доставка</label>
              <label><input class="uk-radio" type="radio" :value="false" v-model="order.delivery"
                            name="delivery">Самовывоз</label>
            </div>
            <div class="uk-margin" v-if="order.delivery">
              <label class="uk-form-label" for="client-address">Адрес</label>
              <div class="uk-form-controls">
                <input class="uk-input" required v-model="order.address" id="client-address"
                       type="text"
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
              данных в соответствии с указанным <a href="/policy/" target="_blank">здесь</a>
              текстом.
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
    import { mapGetters, mapActions } from 'vuex'

    export default {
        name: 'checkout',
        data: () => ({
            order: {
                name: '',
                phone: '',
                address: '',
                person: 1,
                send: false,
                delivery: true,
            },
            page: {
                content: '<div>Загрузка...</div>'
            }
        }),
        mounted () {
            this.getPage()
        },
        computed: {
            ...mapGetters({
                cart: 'cart'
            })
        },
        methods: {
            async getPage () {
                await this.$axios.get(`/api/pages/dostavka/`)
                    .then(res => {
                        this.page = res.data
                    })
            },
            changeQuantity (item, $event) {
                this.updateItemCart({ id: item.id, quantity: $event.target.valueAsNumber })
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
  .cart-item {
    padding-top: 10px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ddd;
    width: 100%;
    margin: 0;
  }

  .cart-item:first-child {
    border-top: 1px solid #ddd;
  }
</style>

<template>
  <div id="products">
    <category-bar :active-category="category"></category-bar>
    <div
      class="uk-flex uk-flex-center uk-flex-wrap uk-grid-match uk-grid-small uk-child-width-1-2 uk-child-width-1-4@m uk-child-width-1-5@l uk-margin">
      <div v-for="product in products" :key="product.id">
        <div class="uk-card uk-position-relative">
          <label class="uk-position-top-right product-label" v-if="product.label">{{product.label}}</label>
          <div class="uk-card-media-top uk-cover-container" v-if="product.image">
            <canvas height="250"></canvas>
            <img :src="product.image" :alt="product.title" uk-cover>
          </div>
          <div class="uk-card-small uk-text-center">
            <h3 class="uk-h5 uk-margin-remove">{{product.title}}</h3>
            <small>{{product.short_desc}}</small>
            <div style="min-height: 40px;"></div>
            <div class="uk-position-bottom-center uk-margin">
              <strong>{{product.price}} руб.</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="uk-flex uk-flex-center" v-if="loading">
      <div>
        <div class="uk-card uk-card-body">
          <span uk-spinner="ratio: 4.5"></span>
        </div>
      </div>
    </div>
    <div class="uk-flex uk-flex-center uk-margin" v-if="loadMore">
      <button @click="getMore" class="uk-button uk-button-default btn-more">Показать еще</button>
    </div>
  </div>
</template>

<script>
  import CategoryBar from '../components/CategoryBar'

  export default {
    name: 'products',
    data() {
      return {
        category: null,
        products: [],
        loadMore: '',
        loading: true
      }
    },
    components: {
      CategoryBar
    },
    created() {
      this.category = categoryId
      this.getProducts(this.category)
      this.loading = false
    },
    methods: {
      async getProducts(category) {
        await this.$axios.get(`/api/products?category=${category}`)
          .then(res => {
            this.products = res.data.results
            this.loadMore = res.data.next
          })
      },
      async getMore() {
        this.loading = true
        await this.$axios.get(this.loadMore)
          .then(res => {
            this.products = [...this.products, ...res.data.results]
            this.loadMore = res.data.next
          })
        this.loading = false
      }
    }
  }
</script>

<style scoped>

</style>

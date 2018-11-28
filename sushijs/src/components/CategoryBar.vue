<template>
  <div class="category-bar">
    <div class="uk-flex uk-flex-wrap">
      <div class="category-item" v-for="category in categories" :key="category.id">
        <a :href="category.url" class="category-btn" :title="category.title"
           :class="{ active: category.id == activeCategory, promo: category.is_promo}">
          {{category.title}}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'category-bar',
    props: ['activeCategory'],
    data() {
      return {
        categories: []
      }
    },
    created() {
      this.getCategories()
    },
    methods: {
      getCategories() {
        this.$axios.get(`/api/categories`)
          .then(res => {
            this.categories = res.data.results
          })
      }
    }
  }
</script>

<style scoped>

</style>

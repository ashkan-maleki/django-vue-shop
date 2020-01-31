<template>
  <div class="row" id="app">
    <div class="col-md-4">
      <ul>
        <li v-for="product in products" :key="product.id">{{ product.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      products: []
    };
  },
  created() {
    this.$http
      .get("http://127.0.0.1:8000/stock/products/", {
        crossdomain: true
      })
      .then(response => {
        console.log(response.body);
        this.products = response.body;
      });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>

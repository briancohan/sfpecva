<template>
  <SiteHeader class="container" />
  <main id="site-main" class="container">
    <router-view />
  </main>
  <SiteFooter />
</template>

<script>
import SiteHeader from "@/components/SiteHeader.vue";
import SiteFooter from "@/components/SiteFooter.vue";

export default {
  components: {
    SiteHeader,
    SiteFooter,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0 auto;
}

.container {
  max-width: 960px;
  margin: 0 auto;
}
</style>

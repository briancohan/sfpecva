<template>
  <SiteHeader />
  <router-view />
</template>

<script>
import SiteHeader from "@/components/SiteHeader.vue";

export default {
  components: {
    SiteHeader,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 960px;
  margin: 0 auto;
}
</style>

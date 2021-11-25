<template>
  <div id="nav">
    <router-link :to="{ name: 'Home' }">Home</router-link>
    <router-link :to="{ name: 'Meetings' }">Meetings</router-link>
    <router-link :to="{ name: 'About' }">About</router-link>
  </div>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 960px;
  margin: 0 auto;
}

#nav {
  padding: 30px;
  display: flex;
  justify-content: space-between;
  max-width: 500px;
  margin: 0 auto;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<template>
  <div id="nav">
    <router-link :to="{ name: 'Home' }">Home</router-link>
    <router-link :to="{ name: 'Meetings' }">Meetings</router-link>
    <router-link :to="{ name: 'About' }">About</router-link>
  </div>
  <div class="banner">
    <img
      id="banner-img"
      alt="rva-skyline"
      src="https://sfpecentralva.org/theme/images/skyline.jpg"
    />
    <a href="https://sfpecentralva.org/">
      <img
        id="logo"
        alt="logo"
        src="https://sfpecentralva.org/theme/images/sfpecva.gif"
      />
    </a>
  </div>
</template>

<style>
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

.banner {
  position: relative;
  height: 250px;
  display: block;
  overflow: hidden;
}

#banner-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

#logo {
  position: absolute;
  top: 5px;
  left: 5px;
  padding: 12px;
  max-height: 170px;
}
</style>

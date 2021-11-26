<template>
  <footer id="site-footer">
    <div class="container">
      <a
        class="centered"
        target="_blank"
        href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=V6CYLBB5B7FB2"
      >
        <h2>Join Our Chapter!</h2>
        <p>Dues are $25 and you do not need to be a member of National SFPE.</p>
      </a>

      <a
        class="centered"
        target="_blank"
        href="https://forms.gle/brDCUowrh4wpAPVc8"
      >
        <h2>Interested in Presenting?</h2>
      </a>

      <div class="links">
        <ul>
          <li><router-link :to="{ name: 'Topics' }">Topics</router-link></li>
          <li>
            <router-link :to="{ name: 'Presenters' }">Presenters</router-link>
          </li>
        </ul>
        <ul>
          <li><a href="#">National SFPE</a></li>
          <li><a href="#">SFPE Job Listings</a></li>
        </ul>
      </div>
    </div>
  </footer>
</template>

<style scoped>
#site-footer {
  background: #aaa;
  color: #333;
}

a {
  color: #333;
}
a:hover {
  color: #111;
}

#site-footer .links {
  display: flex;
  width: 100%;
  justify-content: space-around;
}

li {
  list-style: none;
}

.centered {
  text-align: center;
}
</style>

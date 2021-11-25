<template>
  <div class="officer">
    <img :src="img" alt="{{ name}}" />
    <div class="info">
      <h3>{{ name }}</h3>
      <h4>{{ positions }}</h4>
      <p>{{ bio }}</p>
      <a :href="'//' + linkedin" target="_blank"> LinkedIn </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChapterOfficer",
  props: {
    officer: Object,
  },
  computed: {
    linkedin() {
      return this.officer.LinkedIn[0];
    },
    name() {
      return this.officer.Name[0];
    },
    positions() {
      return this.officer.Position.join(", ");
    },
    bio() {
      return this.officer.Bio[0];
    },
    img() {
      return this.officer.Image[0].url;
    },
  },
};
</script>

<style scoped>
.officer {
  margin-bottom: 5rem;
  display: flex;
  align-items: center;
  gap: 3rem;
}

img {
  max-height: 200px;
  max-width: 200px;
  border-radius: 50%;
}
</style>

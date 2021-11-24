<template>
  <li class="award">
    <span class="award__year">{{ award.Year }}</span>
    <span class="award__name">{{ award.Name }}</span>
  </li>
</template>

<script>
export default {
  name: "ChapterAward",
  props: {
    award: Object,
  },
};
</script>

<style scoped>
.award {
  height: 1.5rem;
}
.award__year {
  margin-right: 1ch;
}
</style>

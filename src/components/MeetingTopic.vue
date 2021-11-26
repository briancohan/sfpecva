<template>
  <div class="topic">
    <h2>
      <span class="tag">{{ tag }}</span
      ><span class="n-events">{{ events }}</span>
    </h2>
    <ul>
      <li v-for="meeting in meetings" :key="meeting">
        <span class="title">{{ meeting.title }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import { format } from "date-fns";

export default {
  name: "MeetingTopic",
  props: {
    topic: Object,
  },
  computed: {
    tag() {
      return this.topic.Name;
    },
    events() {
      if (this.topic.Events === 1) {
        return this.topic.Events + " Meeting";
      } else {
        return this.topic.Events + " Meetings";
      }
    },
    meetings() {
      const titles = this.topic.Titles;
      const dates = this.topic.Dates;

      return titles.map((title, ix) => {
        const date = new Date(dates[ix]);
        return {
          title: title,
          date: format(date, "yyyy-MM-dd"),
        };
      });
    },
  },
};
</script>

<style scoped>
.n-events {
  margin-left: 1rem;
  font-size: 0.8rem;
}
.topic ul {
  display: none;
}

.topic:hover ul {
  display: block;
}
</style>

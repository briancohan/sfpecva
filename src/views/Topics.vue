<template>
  <h1>Topics</h1>
  <MeetingTopic v-for="topic in topics" :key="topic.Name" :topic="topic" />
</template>

<script>
import MeetingTopic from "@/components/MeetingTopic.vue";
import AirtableAPI from "@/services/AirtableAPI.js";

export default {
  name: "Topics",
  components: { MeetingTopic },
  data() {
    return {
      topics: [],
    };
  },
  created() {
    AirtableAPI.getAllTopics().then((response) => {
      this.topics = response.map((award) => award.fields);
    });
  },
};
</script>

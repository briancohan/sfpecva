<template>
  <div class="about">
    <h1>About</h1>
    <p>
      Chapter members and meeting attendees include representatives from a wide
      variety of professions including engineering, consulting, insurance, fire
      protection contractors, and authorities having jurisdiction (AHJs).
    </p>
    <p>
      We collaborate with other professional societies such as the American
      Society of Safety Engineers (ASSE) and the American Society of Plumbing
      Engineers (ASPE). We also participate with the Richmond Joint Engineer’s
      Council to promote engineering careers to high school and middle school
      students.
    </p>
    <p>
      We provide continuing education credit to attendees at our monthly meeting
      seminars. It is the attendee’s responsibility to verify that the seminar
      is appropriate to qualify as continuing education for their profession.
    </p>
    <p>
      We welcome everyone to our meetings! Membership is not necessary to attend
      the meetings, but we encourage you to join and support “engineering a fire
      safe world”.
    </p>
    <p>We are a non-profit organization.</p>
  </div>
  <div class="awards">
    <h2>Awards</h2>
    <ul>
      <ChapterAward v-for="award in awards" :key="award.Key" :award="award" />
    </ul>
  </div>
  <div class="officers">
    <h2>Officers</h2>
    <ChapterOfficer
      v-for="officer in officers"
      :key="officer.Key"
      :officer="officer"
    />
  </div>
</template>

<script>
import ChapterAward from "@/components/ChapterAward.vue";
import ChapterOfficer from "@/components/ChapterOfficer.vue";
import AirtableAPI from "@/services/AirtableAPI.js";

export default {
  name: "About",
  components: { ChapterAward, ChapterOfficer },
  data() {
    return {
      awards: [],
      officers: [],
    };
  },
  created() {
    AirtableAPI.getAllAwards().then((response) => {
      this.awards = response.map((award) => award.fields);
    });
    AirtableAPI.getAllOfficers().then((response) => {
      this.officers = response.map((officer) => officer.fields);
    });
  },
};
</script>

<style scoped>
.awards ul {
  padding-left: 0;
}
.awards li {
  list-style-type: none;
}
</style>

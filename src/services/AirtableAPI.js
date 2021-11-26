const Airtable = require("airtable");

Airtable.configure({
  endpointUrl: "https://api.airtable.com",
  apiKey: process.env.VUE_APP_AIRTABLE_API_KEY,
});

const base = Airtable.base("appQVrGH82zKr13qR");

export default {
  getAllAwards() {
    return base("Awards").select({ view: "All" }).all();
  },
  getAllOfficers() {
    return base("Officers").select({ maxRecords: 100, view: "Current" }).all();
  },
  getAllTopics() {
    return base("Topics").select({ view: "All" }).all();
  },
};

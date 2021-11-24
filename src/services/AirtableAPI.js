const Airtable = require("airtable");

Airtable.configure({
  endpointUrl: "https://api.airtable.com",
  apiKey: process.env.VUE_APP_AIRTABLE_API_KEY,
});

const base = Airtable.base("appQVrGH82zKr13qR");
const awards = base("Awards");

export default {
  getAllAwards() {
    return awards.select({ view: "Grid view" }).all();
  },
};

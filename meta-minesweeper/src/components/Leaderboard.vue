<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ol>
      <router-link
        tag="li"
        :to="{ name: 'player', params: { id: item.bbbv } }"
        v-for="(item, i) in leaderboard"
        :key="i"
        >{{ item.player }} -- {{ item.bbbv }} -- {{ item.rtime }}<br
      /></router-link>
      <!-- <li v-for="(item, i) in leaderboard" :key="i">{{ item.player }} -- {{ item.bbbv }} -- {{ item.rtime }}</li> -->
    </ol>
  </div>
</template>

<script>
import { onMounted } from "vue";
import jsonData from "/static/v.json";
export default {
  name: "Leaderboard",
  props: {
    msg: String,
  },
  setup() {
    onMounted(() => {
      // commonJson = jsonData;
      // console.log(commonJson);
      console.log(jsonData);
    });
  },
  data() {
    return {
      leaderboard: jsonData,
    };
  },
};
</script>





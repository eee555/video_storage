<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ol>
      <router-link
        tag="li"
        :to="{ name: 'player', params: { id: i } }"
        v-for="(item, i) in leaderboard"
        :key="i"
        ><LeaderboardItem :player=i :item=item></LeaderboardItem
      ></router-link>
      <!-- <li v-for="(item, i) in leaderboard" :key="i">{{ item.player }} -- {{ item.bbbv }} -- {{ item.rtime }}</li> -->
    </ol>
  </div>
</template>

<script>
import { onMounted } from "vue";
import jsonData from "/static/l.json";
import LeaderboardItem from "@/components/LeaderboardItem.vue";
export default {
  name: "Leaderboard",
  components: { LeaderboardItem },
  props: {
    msg: String,
  },
  // setup() {
  //   onMounted(() => {
  //     // commonJson = jsonData;
  //     // console.log(commonJson);
  //     console.log(jsonData);
  //   });
  // },
  data() {
    return {
      leaderboard: jsonData,
    };
  },
};
</script>





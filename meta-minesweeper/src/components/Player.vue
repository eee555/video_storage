<template>
  <div class="about">
    <h1>{{ $route.params.id }}</h1>
  </div>
</template>

<script>
import { onMounted } from "vue";
import jsonData from "/static/v.json";
export default {
  name: "PlayerHome",
  //   props: {
  //     msg: String,
  //   },
  setup() {
    onMounted(() => {
      // commonJson = jsonData;
      // console.log(commonJson);
    //   this.$route;
    //   this.data = jsonData[this.$route];
        // console.log(this.$route);
    });
  },
  data() {
    return {
      leaderboard: jsonData,
    };
  },
};
</script>
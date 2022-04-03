<template>
  <div>
    {{ player }} -- {{ item.beg_time }} -- {{ item.beg_bbbv_s }} --
    {{ item.int_time }} -- {{ item.int_bbbv_s }} -- {{ item.exp_time }} --
    {{ item.exp_bbbv_s }}
    <n-button>naive-ui</n-button>
  </div>
</template>

<script>
import { onMounted } from "vue";
// import jsonData from "/static/l.json";
export default {
  name: "LeaderboardItem",
  props: {
    player: String,
    item: Object,
  },
  //   setup(props) {
  //     onMounted(() => {
  //       // commonJson = jsonData;
  //       // console.log(commonJson);
  //       console.log(props.item);
  //     });
  //   },
  // data() {
  //   return {
  //     leaderboard: jsonData,
  //   };
  // },
};
</script>





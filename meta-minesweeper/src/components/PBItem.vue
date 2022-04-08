<template>
  <router-link :to="{ name: 'video', params: { file: pb.file } }">
    <div id="pb_item" :style="classArray">
      <div id="bbbv">{{ bbbv }}</div>
      <div id="para" v-if="para == 0">{{ pb.level }}</div>
      <div id="para" v-else-if="para == 1">{{ pb.bvs.toFixed(2) }}</div>
      <div id="para" v-else-if="para == 2">{{ pb.stnb.toFixed(2) }}</div>
      <div id="para" v-else-if="para == 3">{{ pb.rqp.toFixed(2) }}</div>
      <br />
      <p align="center" id="time">{{ pb.rtime.toFixed(2) }}s</p>
    </div></router-link
  >
</template>

<script>
import { onMounted, ref, computed, watch, onUpdated } from "vue";
import { get_color } from "../utils/color";
// import LeaderboardItem from "@/components/LeaderboardItem.vue";
export default {
  name: "PBItem",
  //   components: { LeaderboardItem },
  props: {
    bbbv: String,
    pb: Object,
    para: Number,
  },
  setup(props) {
    // let classArray = ref("background-color: rgb(0, 255, 255);");
    let classArray = computed({
      get: () => {
        let rgb = get_color(props.pb, props.para);
        // console.log(rgb);
        return `background-color: rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]});`;
      },
    });
    // onUpdated(() => {
    // commonJson = jsonData;
    // console.log(commonJson);
    // let rgb;
    // rgb = get_color(props.pb, props.para);
    // console.log(rgb);
    // classArray = `background-color: rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]});`;
    // console.log(classArray);
    // });
    return {
      classArray,
    };
  },
};
</script>

<style>
#pb_item {
  max-width: 200px;
  padding: 0;
  border: 1px solid rgba(0, 0, 0, 0.18);
  border-radius: 6px;
  margin: 1px;
}
#bbbv {
  margin: 3px;
  font-size: 16px;
  text-align: left;
  display: inline;
  float: left;
}
#para {
  margin: 3px;
  font-size: 16px;
  text-align: right;
  display: inline;
  float: right;
}
#time {
  margin: 2px;
  font-size: 20px;
  margin: 9px 0px 3px 0px;
}

/* .router-link-active {
  text-decoration: none;
  color: black;
} */
a{
  text-decoration: none;
  color: black;
}
</style>















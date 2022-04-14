<template>
  <router-link :to="{ name: 'video_', params: { file: pb.file } }">
    <div id="pb_item" :style="classArray">
      <div id="bbbv">{{ bbbv }}</div>
      <div id="para" v-if="para == 0">{{ pb.level }}</div>
      <div id="para" v-else-if="para == 1">{{ pb.bvs.toFixed(2) }}</div>
      <div id="para" v-else-if="para == 2">{{ pb.stnb.toFixed(2) }}</div>
      <div id="para" v-else-if="para == 3">{{ pb.rqp.toFixed(2) }}</div>
      <br />
      <div align="center" id="time">{{ pb.rtime.toFixed(2) }}s</div>
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
  border: 1px solid rgba(0, 0, 0, 0.18);
  border-radius: 6px;
  margin: 3px;
}
#bbbv {
  margin-left: 3px;
  font-size: 16px;
  text-align: left;
  /* display: inline; */
  float: left;
  padding: 0px;
}
#para {
  margin-right: 3px;
  font-size: 16px;
  text-align: right;
  /* display: inline; */
  float: right;
  padding: 0px;
}
#time {
  font-size: 20px;
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















<template>
  <router-link :to="{ name: 'game_', params: { file: video.file } }">
    <div id="video_item" :style="classArray">
      <p align="center" id="time">{{ value }}</p>
    </div></router-link
  >
</template>

<script>
import { onMounted, ref, computed, watch, onUpdated } from "vue";
import { get_color } from "../utils/color";
// import LeaderboardItem from "@/components/LeaderboardItem.vue";
export default {
  name: "VideoBlock",
  props: {
    video: Object,
    para: String,
  },
  setup(props) {
    if (props.video.row == 8) {
      props.video.level = "beg";
    } else if (props.video.row == 16 && props.video.column == 16) {
      props.video.level = "int";
    } else if (props.video.row == 16 && props.video.column == 30) {
      props.video.level = "exp";
    }
    let value = computed({
      get: () => {
        return props.video[props.para].toFixed(2);
      },
    });
    let classArray = computed({
      get: () => {
        let rgb = get_color(props.video, props.para);
        return `background-color: rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]});`;
      },
    });
    return {
      classArray,
      value,
    };
  },
};
</script>

<style>
#video_item {
  max-width: 200px;
  border-radius: 0px;
  margin: 0px;
  padding: 0px;
}
#time{
  padding: 0;
  margin: 0px;
}


/* .router-link-active {
  text-decoration: none;
  color: black;
} */
a {
  text-decoration: none;
  color: black;
}
</style>















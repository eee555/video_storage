<template>
  <div id="leaderboard_body">
    <!-- <n-card size="small">
      <n-el
        tag="span"
        style="color: black; transition: 0.3s var(--cubic-bezier-ease-in-out)"
      > -->
        <n-row gutter="3">
          <n-col :span="6">
            <div>{{ player }}</div>
          </n-col>
          <n-col :span="3">
            <div>
              <router-link
                v-if="item.beg_time[1]"
                :to="{ name: 'video', params: { file: item.beg_time[1] } }"
                class="score"
                >{{ Math.round(item.beg_time[0] * 100) / 100 }}</router-link
              ><template v-else class="score"> 10 </template>
            </div>
          </n-col>
          <n-col :span="3">
            <div>
              <router-link
                v-if="item.beg_bbbv_s[1]"
                :to="{ name: 'video', params: { file: item.beg_bbbv_s[1] } }"
                >{{ Math.round(item.beg_bbbv_s[0] * 100) / 100 }}</router-link
              ><template v-else> 2 </template>
            </div>
          </n-col>
          <n-col :span="3">
            <div>
              <router-link
                v-if="item.int_time[1]"
                :to="{ name: 'video', params: { file: item.int_time[1] } }"
                >{{ Math.round(item.int_time[0] * 100) / 100 }}</router-link
              ><template v-else> 60 </template>
            </div>
          </n-col>
          <n-col :span="3">
            <router-link
              v-if="item.int_bbbv_s[1]"
              :to="{ name: 'video', params: { file: item.int_bbbv_s[1] } }"
              >{{ Math.round(item.int_bbbv_s[0] * 100) / 100 }}</router-link
            ><template v-else> 1 </template>
          </n-col>
          <n-col :span="3">
            <router-link
              v-if="item.exp_time[1]"
              :to="{ name: 'video', params: { file: item.exp_time[1] } }"
              >{{ Math.round(item.exp_time[0] * 100) / 100 }}</router-link
            ><template v-else> 240 </template>
          </n-col>
          <n-col :span="3">
            <router-link
              v-if="item.exp_bbbv_s[1]"
              :to="{ name: 'video', params: { file: item.exp_bbbv_s[1] } }"
              >{{ Math.round(item.exp_bbbv_s[0] * 100) / 100 }}</router-link
            ><template v-else> 0.5 </template>
          </n-col>
        </n-row>
      <!-- </n-el>
    </n-card> -->
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

<style>
.score {
  /* border: 1px solid;
  border-radius: 3px; */
  tab-size: 4;
  margin: auto;
}
#leaderboard_body {
  /* border: 1px solid;
  border-radius: 3px; */
  /* width: 80%; */
  margin: 8px auto;
}
</style>



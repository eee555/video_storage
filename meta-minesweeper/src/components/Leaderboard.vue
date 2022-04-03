<template>
  <div id="hello">
    <h1>{{ msg }}</h1>
    <n-tabs type="segment">
      <n-tab-pane name="chap1" tab="（名字还没想好的）扫雷网">
        <ol id="leaderboard_item">
          <n-row gutter="3">
            <n-col :span="6">
              <p>姓名</p>
            </n-col>
            <n-col :span="3">
              <p>初级时间</p>
            </n-col>
            <n-col :span="3">
              <p>3BV/s</p>
            </n-col>
            <n-col :span="3">
              <p>中级时间</p>
            </n-col>
            <n-col :span="3"> <p>3BV/s</p> </n-col>
            <n-col :span="3">
              <p>高级时间</p>
            </n-col>
            <n-col :span="3">
              <p>3BV/s</p>
            </n-col>
          </n-row>
          <!-- <router-link
        tag="li"
        :to="{ name: 'player', params: { id: i } }"
        v-for="(item, i) in leaderboard"
        :key="i"
        ><LeaderboardItem :player=i :item=item></LeaderboardItem
      ></router-link> --><LeaderboardItem
            :player="i"
            :item="item"
            v-for="(item, i) in leaderboard"
            :key="i"
          ></LeaderboardItem>
          <!-- <li v-for="(item, i) in leaderboard" :key="i">{{ item.player }} -- {{ item.bbbv }} -- {{ item.rtime }}</li> -->
        </ol>
      </n-tab-pane>
      <n-tab-pane name="chap2" tab="国际网排行榜">
        <div>这里爬一份国际网排行榜</div>
      </n-tab-pane>
      <n-tab-pane name="chap3" tab="扫雷网排行榜">
        <div>这里爬一份扫雷网排行榜</div>
      </n-tab-pane>
    </n-tabs>
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

<style>
#hello {
  width: 61%;
  margin: 10px auto;
}
#leaderboard_item {
  /* border: 1px solid;
  border-radius: 3px; */
  width: 75%;
  margin: 10px auto;
  padding: 0px;
}
</style>



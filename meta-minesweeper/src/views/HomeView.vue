<template>
  <div class="home">
    <n-carousel autoplay dot-type="line">
      <img
        class="carousel-img"
        src="../assets/p1.png"
        style="width: 100%; height: 20%"
      />
      <img
        class="carousel-img"
        src="../assets/p2.png"
        style="width: 100%; height: 20%"
      />
      <img
        class="carousel-img"
        src="../assets/p3.png"
        style="width: 100%; height: 20%"
      />
    </n-carousel>

    <n-tabs type="segment" style="width: 80%;margin: 0px auto;" tab-style="font-size:24px;">
      <n-tab-pane name="chap1" tab="我的PB">
        <PBTable></PBTable>
      </n-tab-pane>
      <n-tab-pane name="chap2" tab="比赛">
        <CurrentGame></CurrentGame>
      </n-tab-pane>
      <n-tab-pane name="chap3" tab="没想好">
        <div>这里没想好</div>
      </n-tab-pane>
    </n-tabs>
  </div>
</template>

<script>
// @ is an alias to /src
// import Leaderboard from '@/components/Leaderboard.vue'
import PBTable from "@/components/PBTable.vue";
import CurrentGame from "@/components/CurrentGame.vue";
export default {
  name: "HomeView",
  components: {
    PBTable,
    CurrentGame,
  },
};
</script>

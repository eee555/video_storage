<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/network.svg" width="600" height="360">
    <!-- <Leaderboard msg="（名字还没想好的）扫雷网"/> -->
    <PBTable></PBTable>

  </div>
</template>

<script>
// @ is an alias to /src
// import Leaderboard from '@/components/Leaderboard.vue'
import PBTable from '@/components/PBTable.vue'
export default {
  name: 'HomeView',
  components: {
    PBTable
  }
}
</script>

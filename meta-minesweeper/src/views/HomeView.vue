<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <Leaderboard msg="（名字还没想好的）扫雷网"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Leaderboard from '@/components/Leaderboard.vue'

export default {
  name: 'HomeView',
  components: {
    Leaderboard
  }
}
</script>

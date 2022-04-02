<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Leaderboard msg="Welcome to Your Vue.js App"/>
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

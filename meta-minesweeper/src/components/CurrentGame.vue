<template>
  <div id="hello">
    <template>
      <n-skeleton text :repeat="2" /> <n-skeleton text style="width: 100%" />
    </template>

  </div>
</template>
  </div>
</template>

<script>
import { onMounted, reactive, onBeforeMount } from "vue";
import allData from "/static/v.json";
// import colorFileName from "@/assets/color.png";
import PBItem from "@/components/PBItem.vue";
// import axios from 'axios'

// stnb,rqp,3bvs,time
export default {
  name: "CurrentGame",
  //   components: { PBItem },
  props: {
    msg: String,
  },
  setup() {},
};
</script>

<style>
#hello {
  width: 100%;
  margin: 10px auto;
}
</style>











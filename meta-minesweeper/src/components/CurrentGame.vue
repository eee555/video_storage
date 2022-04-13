<template>
  <div id="hello">
    <template>
      <n-skeleton text :repeat="2" /> <n-skeleton text style="width: 100%" />
    </template>
    <div style="display: inline; float: left;list-style:none;">
      <h1>初级</h1>
      <li v-for="(item, i) in beg_data" :key="i">
        {{ item.rtime.toFixed(2) }}
      </li>
    </div>
    <div style="display: inline; float: left; margin-left: 50px; list-style:none;">
      <h1>中级</h1>
      <li v-for="(item, i) in int_data" :key="i">
        {{ item.rtime.toFixed(2) }}
      </li>
    </div>
    <div style="display: inline; float: left; margin-left: 50px; list-style:none;">
      <h1>高级</h1>
      <li v-for="(item, i) in exp_data" :key="i">
        {{ item.rtime.toFixed(2) }}
      </li>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive, onBeforeMount, ref, computed } from "vue";
import allData from "/static/tournament.json";
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
  setup() {
    let beg_num = ref(20);
    let int_num = ref(10);
    let exp_num = ref(5);
    let para = reactive({
      beg: "time",
      int: "time",
      exp: "time",
    });
    let beg_data = allData.filter((v) => {
      return v.row == 8 && v.column == 8 && v.mine_num == 10 && v.bbbv >= 10;
    });
    let int_data = allData.filter((v) => {
      return v.row == 16 && v.column == 16 && v.mine_num == 40 && v.bbbv >= 30;
    });
    let exp_data = allData.filter((v) => {
      return v.row == 16 && v.column == 30 && v.mine_num == 99 && v.bbbv >= 100;
    });
    // console.log(sorted_beg_time);
    // sorted_beg_time.sort(function (a, b) {
    //   return a.rtime - b.rtime;
    // });
    // console.log(sorted_beg_time);
    let beg_value = computed(() => {
      return 2;
    });

    return {
      beg_num,
      int_num,
      exp_num,
      beg_data,
      int_data,
      exp_data,
    };
  },
  data() {
    return {
      allData: allData,
    };
  },
};
</script>

<style>
#hello {
  width: 100%;
  margin: 10px auto;
}
</style>











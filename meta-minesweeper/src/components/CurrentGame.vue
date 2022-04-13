<template>
  <div id="hello">
    <template>
      <n-skeleton text :repeat="2" /> <n-skeleton text style="width: 100%" />
    </template>

    <button :class="{ selected: para == 'rtime' }" @click="changePara('rtime')">
      time
    </button>
    <button :class="{ selected: para == 'bvs' }" @click="changePara('bvs')">
      3BV/s
    </button>
    <button :class="{ selected: para == 'stnb' }" @click="changePara('stnb')">
      STNB
    </button>
    <button :class="{ selected: para == 'rqp' }" @click="changePara('rqp')">
      RQP
    </button>
    <br />

    <div style="display: inline; float: left; list-style: none">
      <h1>初级</h1>
      <li v-for="(item, i) in beg_data" :key="i">
        <VideoBlock :video="item" :para="para"></VideoBlock>
      </li>
    </div>
    <div
      style="display: inline; float: left; margin-left: 50px; list-style: none"
    >
      <h1>中级</h1>
      <li v-for="(item, i) in int_data" :key="i">
        <VideoBlock :video="item" :para="para"></VideoBlock>
      </li>
    </div>
    <div
      style="display: inline; float: left; margin-left: 50px; list-style: none"
    >
      <h1>高级</h1>
      <li v-for="(item, i) in exp_data" :key="i">
        <VideoBlock :video="item" :para="para"></VideoBlock>
      </li>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive, onBeforeMount, ref, computed } from "vue";
import allData from "/static/tournament.json";
// import colorFileName from "@/assets/color.png";
import VideoBlock from "@/components/VideoBlock.vue";
// import axios from 'axios'

// stnb,rqp,3bvs,time
export default {
  name: "CurrentGame",
  components: { VideoBlock },
  props: {
    msg: String,
  },
  setup() {
    let beg_num = ref(20);
    let int_num = ref(10);
    let exp_num = ref(5);
    let para = ref("rtime");
    let beg_data = allData.filter((v) => {
      return v.row == 8 && v.column == 8 && v.mine_num == 10 && v.bbbv >= 10;
    });
    let int_data = allData.filter((v) => {
      return v.row == 16 && v.column == 16 && v.mine_num == 40 && v.bbbv >= 30;
    });
    let exp_data = allData.filter((v) => {
      return v.row == 16 && v.column == 30 && v.mine_num == 99 && v.bbbv >= 100;
    });

    beg_data.forEach((v) => {
      v.bvs = v.bbbv_s;
      if (v.row == 8) {
        v.stnb = 47.22 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      } else if (v.row == 16 && v.column == 16) {
        v.stnb = 153.73 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      } else if (v.row == 16 && v.column == 30) {
        v.stnb = 435.001 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      }
      v.rqp = v.rtime*v.rtime/v.bbbv;
    });
    int_data.forEach((v) => {
      v.bvs = v.bbbv_s;
      if (v.row == 8) {
        v.stnb = 47.22 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      } else if (v.row == 16 && v.column == 16) {
        v.stnb = 153.73 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      } else if (v.row == 16 && v.column == 30) {
        v.stnb = 435.001 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      }
      v.rqp = v.rtime*v.rtime/v.bbbv;
    });
    exp_data.forEach((v) => {
      v.bvs = v.bbbv_s;
      if (v.row == 8) {
        v.stnb = 47.22 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      } else if (v.row == 16 && v.column == 16) {
        v.stnb = 153.73 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      } else if (v.row == 16 && v.column == 30) {
        v.stnb = 435.001 / (Math.pow(v.rtime, 1.7) / v.bbbv);
      }
      v.rqp = v.rtime*v.rtime/v.bbbv;
    });

    return {
      beg_num,
      int_num,
      exp_num,
      beg_data,
      int_data,
      exp_data,
      para,
    };
  },
  data() {
    return {
      allData: allData,
      changePara: (p) => {
        this.para = p;
        if (p == "rtime" || p == "rqp") {
          this.beg_data.sort(function (a, b) {
            return a[p] - b[p];
          });
          this.int_data.sort(function (a, b) {
            return a[p] - b[p];
          });
          this.exp_data.sort(function (a, b) {
            return a[p] - b[p];
          });
        } else if (p == "bvs" || p == "stnb") {
          this.beg_data.sort(function (a, b) {
            return b[p] - a[p];
          });
          this.int_data.sort(function (a, b) {
            return b[p] - a[p];
          });
          this.exp_data.sort(function (a, b) {
            return b[p] - a[p];
          });
        }
      },
    };
  },
};
</script>

<style>
#hello {
  width: 100%;
  margin: 10px auto;
}
.selected {
  background-color: #797979; /* Green */
  color: white;
}
</style>











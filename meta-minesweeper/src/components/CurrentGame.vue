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
    <div
      style="
        display: inline;
        float: left;
        margin-left: 50px;
        list-style: none;
        padding-left: 50px;
        padding-top: 50px;
      "
    >
      <h2>初级局数：</h2>
      <n-input-number
        v-model:beg_num="beg_num"
        clearable
        default-value="20"
        @update:value="begNumChange"
        :min="1"
        :max="beg_data.length"
      />
      <h2>中级局数：</h2>
      <n-input-number
        v-model:int_num="int_num"
        clearable
        default-value="12"
        @update:value="intNumChange"
        :min="1"
        :max="int_data.length"
      />
      <h2>高级局数：</h2>
      <n-input-number
        v-model:exp_num="exp_num"
        clearable
        default-value="5"
        @update:value="expNumChange"
        :min="1"
        :max="exp_data.length"
      />
    </div>
    <div
      style="
        display: inline;
        float: left;
        margin-left: 50px;
        list-style: none;
        padding-left: 50px;
        padding-top: 50px;
      "
    >
      <h4>初级总得分：{{ score_beg_sum.toFixed(2) }}</h4>
      <h4>初级平均得分：{{ (score_beg_sum / beg_num).toFixed(2) }}</h4>
      <h4>中级总得分：{{ score_int_sum.toFixed(2) }}</h4>
      <h4>中级平均得分：{{ (score_int_sum / int_num).toFixed(2) }}</h4>
      <h4>高级总得分：{{ score_exp_sum.toFixed(2) }}</h4>
      <h4>高级平均得分：{{ (score_exp_sum / exp_num).toFixed(2) }}</h4>
      <h4>总得分：{{ score_sum.toFixed(2) }}</h4>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive, onUpdated, ref, computed } from "vue";
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
      v.rqp = (v.rtime * v.rtime) / v.bbbv;
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
      v.rqp = (v.rtime * v.rtime) / v.bbbv;
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
      v.rqp = (v.rtime * v.rtime) / v.bbbv;
    });

    let beg_num = ref(20);
    let int_num = ref(12);
    let exp_num = ref(5);
    let score_beg_sum = computed({
      get: () => {
        let value = beg_data
          .map((item, index) => {
            return item[para.value];
          })
          .slice(0, beg_num.value)
          .reduce((sum, value) => {
            return sum + value;
          }, 0);
        return value;
      },
    });
    let score_int_sum = computed({
      get: () => {
        let value = int_data
          .map((item, index) => {
            return item[para.value];
          })
          .slice(0, int_num.value)
          .reduce((sum, value) => {
            return sum + value;
          }, 0);
        return value;
      },
    });
    let score_exp_sum = computed({
      get: () => {
        let value = exp_data
          .map((item, index) => {
            return item[para.value];
          })
          .slice(0, exp_num.value)
          .reduce((sum, value) => {
            return sum + value;
          }, 0);
        return value;
      },
    });
    let score_sum = computed({
      get: () => {
        return score_beg_sum.value + score_int_sum.value + score_exp_sum.value;
      },
    });

    return {
      beg_num,
      int_num,
      exp_num,
      beg_data,
      int_data,
      exp_data,
      para,
      score_beg_sum,
      score_int_sum,
      score_exp_sum,
      score_sum,
      begNumChange(v) {
        beg_num.value = v;
      },
      intNumChange(v) {
        int_num.value = v;
      },
      expNumChange(v) {
        exp_num.value = v;
      },
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











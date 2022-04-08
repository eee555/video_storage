<template>
  <div class="about">
    <h1>录像分析：{{ $route.params.file }}</h1>
    <div id="row" style="width: 500px; height: 300px"></div>
  </div>
</template>

<script>
import { onMounted, onBeforeMount } from "vue";
import jsonData from "/static/v.json";
import * as echarts from "echarts";
// import * as ms from "ms-toollib";

export default {
  name: "VideoDetail",
  //   props: {
  //     msg: String,
  //   },
  setup() {
    onBeforeMount(() => {
      console.log(ms);
      const get_board = async () => {
        while (board.length > 0) {
          board.pop();
        }
        const ms = await import("ms-toollib");
        const rows = 16;
        const columns = 30;
        let b = JSON.parse(
          ms.laymine_solvable(rows, columns, 99, 0, 0, 100, 381, 10000, 40)
        )[0];
        for (let i = 0; i < rows; i++) {
          board.push([]);
          for (let j = 0; j < columns; j++) {
            board[i].push(b[i][j]);
          }
        }
      };
    });

    onMounted(() => {
      let myChart = echarts.init(document.getElementById("row"));
      // 指定图表的配置项和数据
      let option = {
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: "line",
            smooth: true,
          },
        ],
      };
      myChart.setOption(option);
    });
  },
  data() {
    return {
      leaderboard: jsonData,
    };
  },
};
</script>
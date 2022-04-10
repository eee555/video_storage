<template>
  <div class="about">
    <h1>录像分析</h1>

    <n-table striped style="width: 60%; margin: 0px auto">
      <thead>
        <tr>
          <th>指标</th>
          <th>数值</th>
          <th>指标</th>
          <th>数值</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>标识</td>
          <td>{{ p.player }}</td>
          <td>3BV</td>
          <td>{{ p.bv }}</td>
        </tr>
        <tr>
          <td>rTime</td>
          <td>{{ p.time }}</td>
          <td>3BV/s</td>
          <td>{{ p.bvs }}</td>
        </tr>
        <tr>
          <td>Left/s</td>
          <td>{{ p.lefts }}</td>
          <td>Right/s</td>
          <td>{{ p.rights }}</td>
        </tr>
        <tr>
          <td>Chording/s</td>
          <td>{{ p.chordings }}</td>
          <td>Thrp</td>
          <td>{{ p.thrp }}</td>
        </tr>
      </tbody>
    </n-table>

    <!-- <p class="detail">标识：{{ p.player }}</p>
    <p class="detail">3BV：{{ p.bv }}</p>
    <p class="detail">时间：{{ p.time }}</p>
    <p class="detail">3BV/s：{{ p.bvs }}</p> -->
    <br />
    <div
      id="row"
      style="width: 500px; height: 300px; display: inline-block"
    ></div>
    <div
      id="column"
      style="width: 500px; height: 300px; display: inline-block"
    ></div>
  </div>
  <!-- 代码可从 https://github.com/hgraceb/flop-player/releases 下载 -->
  <iframe
    class="flop-player-iframe flop-player-display-none"
    style="width: 65%; height: 500px"
    src="/video_storage/flop/index.html"
    ref="video_iframe"
  ></iframe>
</template>

<script>
import { onMounted, onBeforeMount, ref, getCurrentInstance } from "vue";
import { get_x_track, get_y_track } from "../utils/get_track";
import jsonData from "/static/v.json";
import * as echarts from "echarts";
// import * as ms from "ms-toollib";

export default {
  name: "VideoDetail",
  //   props: {
  //     msg: String,
  //   },
  props: {
    file: String,
  },
  setup(props) {
    // const iframeWin = getCurrentInstance().ctx.$refs.video_iframe.contentWindow;
    const p = ref({
      player: "",
      time: "",
      bv: "",
      bvs: "",
      lefts: "",
      rights: "",
      chordings: "",
      thrp: "",
    });
    let option_x;
    let option_y;

    const get_ms_toollib = async () => {
      return await import("ms-toollib");
    };
    get_ms_toollib().then((ms) => {
      const request = new XMLHttpRequest();
      request.onload = () => {
        let r = new Uint8Array(request.response);
        let video = ms.AvfVideo.new(r);
        video.parse_video();
        // console.log(video.get_bbbv);
        // console.log(video.get_player);
        video.analyse();
        p.value.player = video.get_player;
        p.value.time = video.get_r_time;
        p.value.bvs = video.get_bbbv_s;
        p.value.bv = video.get_bbbv;
        p.value.lefts = `${video.get_lefts}@${video.get_lefts_s}`;
        p.value.rights = `${video.get_rights}@${video.get_rights_s}`;
        p.value.chordings = `${video.get_chordings}@${video.get_chordings_s}`;
        p.value.thrp = video.get_thrp;

        option_x = get_x_track(video);
        let myChart_row = echarts.init(document.getElementById("row"));
        option_y = get_y_track(video);
        let myChart_column = echarts.init(document.getElementById("column"));

        myChart_row.setOption(option_x);
        myChart_column.setOption(option_y);
      };
      request.onerror = (e) => {
        console.log(555);
      };
      // console.log(props.file);
      request.open("GET", `/video_storage/video/${props.file}`);
      request.responseType = "arraybuffer";
      request.send();
      // console.log(ms.laymine_number(16, 30, 99, 0, 0));
    });
    onBeforeMount(() => {
      // console.log(ms);
      // console.log(ms-toollib)
    });

    onMounted(() => {
      let w = getCurrentInstance().refs.video_iframe.contentWindow;
      console.log(
        props.file
      );
      // 预期是一进入这个页面就自动开始播放props.file这个录像，在iframe标签的位置

      const uri = `../video/${props.file}`
      // 等待 Flop Player 初始化完成
      window.flop = {
        onload: () => {
          // 具体参数说明参见：https://github.com/hgraceb/flop-player#flopplayvideouri-options
          window.flop.playVideo(uri, {
            share: {
              uri: uri,
              pathname: '/flop-player/player',
              anonymous: true,
              background: '#eee',
              title: 'Flop Player Share',
              favicon: 'https://avatars.githubusercontent.com/u/38378650?s=32'
            },
            anonymous: false,
            background: 'rgba(0, 0, 0, .5)',
            listener: function () {
              console.log('Flop player exit')
            }
          })
        }
      }
    });
    return {
      p,
      option_x,
    };
  },
};
</script>

<style>
.detail {
  font-size: 15px;
  margin: 2px 0px 2px 20%;
  text-align: left;
}
</style>



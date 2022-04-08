<template>
  <div id="hello">
    <h1>初级PB({{ Object.keys(pbData.beg).length }})</h1>

    <button :class="{ selected: selected.beg === 0 }" @click="choose('beg', 0)">
      time
    </button>
    <button :class="{ selected: selected.beg === 1 }" @click="choose('beg', 1)">
      3BV/s
    </button>
    <button :class="{ selected: selected.beg === 2 }" @click="choose('beg', 2)">
      STNB
    </button>
    <button :class="{ selected: selected.beg === 3 }" @click="choose('beg', 3)">
      RQP
    </button>

    <n-grid :x-gap="3" :y-gap="3" :cols="10">
      <n-grid-item v-for="(item, i) in pbData.beg" key="i"
        ><PBItem :bbbv="i" :pb="item" :para="selected.beg"></PBItem>
      </n-grid-item>
    </n-grid>

    <h1>中级PB({{ Object.keys(pbData.int).length }})</h1>

    <button :class="{ selected: selected.int === 0 }" @click="choose('int', 0)">
      time
    </button>
    <button :class="{ selected: selected.int === 1 }" @click="choose('int', 1)">
      3BV/s
    </button>
    <button :class="{ selected: selected.int === 2 }" @click="choose('int', 2)">
      STNB
    </button>
    <button :class="{ selected: selected.int === 3 }" @click="choose('int', 3)">
      RQP
    </button>

    <n-grid :x-gap="3" :y-gap="3" :cols="10">
      <n-grid-item v-for="(item, i) in pbData.int" key="i"
        ><PBItem :bbbv="i" :pb="item" :para="selected.int"></PBItem>
      </n-grid-item>
    </n-grid>

    <h1>高级PB({{ Object.keys(pbData.exp).length }})</h1>

    <button :class="{ selected: selected.exp === 0 }" @click="choose('exp', 0)">
      time
    </button>
    <button :class="{ selected: selected.exp === 1 }" @click="choose('exp', 1)">
      3BV/s
    </button>
    <button :class="{ selected: selected.exp === 2 }" @click="choose('exp', 2)">
      STNB
    </button>
    <button :class="{ selected: selected.exp === 3 }" @click="choose('exp', 3)">
      RQP
    </button>

    <n-grid :x-gap="3" :y-gap="3" :cols="10">
      <n-grid-item v-for="(item, i) in pbData.exp" key="i"
        ><PBItem :bbbv="i" :pb="item" :para="selected.exp"></PBItem>
      </n-grid-item>
    </n-grid>
  </div>
</template>

<script>
import { onMounted, reactive, onBeforeMount } from "vue";
import pbData from "/static/pb.json";
// import colorFileName from "@/assets/color.png";
import PBItem from "@/components/PBItem.vue";
// import axios from 'axios'

// stnb,rqp,3bvs,time
export default {
  name: "PBTable",
  components: { PBItem },
  props: {
    msg: String,
  },
  setup() {
    // const button_off = reactive({
    //   color: "black",
    // });
    // const changeColorOn = () => {
    //   button_off.color = "white";
    // };
    onBeforeMount(() => {
      // commonJson = jsonData;
      // console.log(commonJson);
      // console.log(jsonData);

      for (let key in pbData.beg) {
        pbData.beg[key].level = "beg";
        pbData.beg[key].bvs = key / pbData.beg[key].rtime;
        pbData.beg[key].stnb =
          47.22 / (Math.pow(pbData.beg[key].rtime, 1.7) / key);
        pbData.beg[key].rqp =
          (pbData.beg[key].rtime * pbData.beg[key].rtime) / key;
      }
      for (let key in pbData.int) {
        pbData.int[key].level = "int";
        pbData.int[key].bvs = key / pbData.int[key].rtime;
        pbData.int[key].stnb =
          153.73 / (Math.pow(pbData.int[key].rtime, 1.7) / key);
        pbData.int[key].rqp =
          (pbData.int[key].rtime * pbData.int[key].rtime) / key;
      }
      for (let key in pbData.exp) {
        pbData.exp[key].level = "exp";
        pbData.exp[key].bvs = key / pbData.exp[key].rtime;
        pbData.exp[key].stnb =
          435.001 / (Math.pow(pbData.exp[key].rtime, 1.7) / key);
        pbData.exp[key].rqp =
          (pbData.exp[key].rtime * pbData.exp[key].rtime) / key;
      }
    });
    // onMounted(() => {
    //   console.log(colorFileName);
    //   const request = new XMLHttpRequest();
    //   request.onload = () => {
    //     let r = new Uint8Array(request.response);
    //     console.log(r);
    //   };
    //   request.onerror = (e) => {
    //     console.log(555);
    //   };
    //   request.open("GET", colorFileName);
    //   request.responseType = "arraybuffer";
    //   request.send();
    // });
  },

  data() {
    return {
      pbData: pbData,
      selected: { beg: -1, int: -1, exp: -1 },
      choose(level, index) {
        this.selected[level] = index; //获得点击元素的index
      },
    };
  },
};
</script>

<style>
#hello {
  width: 80%;
  margin: 10px auto;
}
#leaderboard_item {
  /* border: 1px solid;
  border-radius: 3px; */
  width: 75%;
  margin: 10px auto;
  padding: 0px;
}
button {
  font-size: 18px;
  width: 100px;
  height: 40px;
  margin: 8px 4px 8px 4px;
  border: 1px solid rgb(123, 123, 123);
  background-color: rgb(227, 227, 227);
  border-radius: 1px;
  color: black;
}
button:hover {
  background-color: #7d7d7d; /* Green */
  color: white;
}
.selected {
  background-color: #797979; /* Green */
  color: white;
}
/* text {
  font-size: 18px;
  margin: 8px 50px 8px 5px;
} */
</style>











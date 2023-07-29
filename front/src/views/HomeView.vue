<script setup>
import Tile from "../components/UI/Tile.vue";
import MyButton from "../components/UI/Button.vue";
</script>

<template>
    <main>
        <h1 class="gradient-multiline
               text-left
               flex flex-col items-start
              ">
            <span class="p1">ПУТЕШЕСТВИЕ</span>
            <span class="p2">на красную планету</span>
        </h1>

        <div class="info">
            <div class="win-grid">
                <Tile v-for="i in tiles"
                      :top_text="i.top_text"
                      :main_text="i.main_text"
                      :bottom_text="i.bottom_text"
                      :id="i.id"
                      :key="i.id"
                />
            </div>
        </div>

        <MyButton class="start_button" id="start_button">
            <span class="z-10">Начать путешествие</span>
        </MyButton>
    </main>


</template>

<script>

import axios from "axios";

export default {
    data() {
        return {
            tiles: [],
            button_x: 0,
            button_y: 0
        }
    },
    beforeMount() {
        axios.get('http://46.161.49.152:8000/info/banner/').then(
            value => this.tiles = value.data
        ).catch(reason => console.error(reason))
    },
    computed: {
        width: function () {
            return window.innerWidth
        },
        height: function () {
            return window.innerHeight
        },
        button_center: function () {
            return document.getElementById("start_button").getBoundingClientRect();
        }
    }
}
</script>

<style scoped lang="scss">

.line {
  position: absolute;
  max-width: 100px;

}

.info {
  position: absolute;
  top: 50%;
  left: 60%;
  transform: translateY(-50%);
  margin-left: -5vw;
}

.start_button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%);
    margin-left: -30vw;

  margin-top: 10vh;
}

.p1, .p2 {
  text-size-adjust: auto;
}

.p1 {
  font-size: 72px;
  min-height: fit-content;
  padding: 30px 0;
}

@media (max-width: 548px) {
  .p1 {
    font-size: 58px;
  }
    .gradient-multiline{
        top: 250px !important;
    }

}



.p2 {
  font-size: 30px;
  padding-bottom: 10px;
}

.gradient-multiline {
  background-color: transparent;
  text-align: start;
  line-height: 1.5em;
  max-width: fit-content;


  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  margin-left: -25%;
  margin-top: -15vh;
}

.gradient-multiline span {
  text-size-adjust: auto;
  color: transparent;
  background: linear-gradient(60deg, white, rgb(251, 56, 12));
  background-clip: text;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;

}


@supports (mix-blend-mode: lighten) {

  .gradient-multiline::after {
    position: absolute;
    content: '';
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    pointer-events: none;
    background: linear-gradient(60deg, white, rgb(251, 70, 12));
    background-clip: text;
    mix-blend-mode: lighten;
  }

}

* {
  box-sizing: border-box;
}


.win-grid {
  letter-spacing: 2px;
  color: white;
  display: grid;
  grid-template-columns: repeat(2, min-content);
  align-items: stretch;
  text-align: center;
  grid-gap: 8px;
  padding: 5rem;
  padding-right: 0;
}


button:focus {
  outline: none;
}

@media (max-width: 1279px) {
  .info {
    left: 50%;
    transform: translateX(-50%);
    margin-left: 0;
  }
  .win-grid {
    padding-left: 0;
  }
  .start_button {
    left: 50%;
    transform: translateX(-50%);
    margin-left: 0;
    margin-top: 1.5rem;
  }
}

@media (max-width: 1024px) {
  .gradient-multiline {
    margin-left: 0;
    margin-top: -45px;
  }
}

@media (max-width: 425px) {
    .p1 {
        font-size: 48px;
    }
    .p2{
        font-size: 24px;
    }
    .gradient-multiline{
        top: 250px !important;
    }
    .info{
        margin-top: 20%;
    }
}

@media (max-width: 345px) {
    .p1{
        font-size: 44px;
    }
    .p2{
        font-size: 20px;
    }
    .info{
        margin-top: 20%;
    }
}


@media (max-width: 302px) {
    .p1{
        font-size: 38px;
    }
    .p2{
        font-size: 18px;
    }
    .info{
        margin-top: 20%;
    }
}
</style>
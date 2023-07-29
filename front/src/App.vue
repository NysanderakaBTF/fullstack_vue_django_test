<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from "@/components/Navbar.vue";
</script>

<template>
  <header>
    <Navbar></Navbar>
  </header>

  <RouterView />
</template>

<style scoped lang="scss">

</style>

<style>
html {
  min-height: 100vh;
}
body{
  min-height: 100vh;
  background-image: url("./assets/newbg.png");
  background-position: top center;
  background-repeat: no-repeat;
  background-size: none;
}

</style>

<script setup>

const props = defineProps({
  name: String,
  link: String
})

</script>

<template>
<a class="underline" :href="props.link">{{props.name}}</a>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

*{
  font-family: 'Poppins', sans-serif;
}

p, a {
  text-align: center;
}

a{
  text-decoration: none;
  color: rgb(255,255,255);
}

a:hover{
  color: rgb(177,177,177);
}

.underline{
  position: relative;
}

.underline::before{
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  width: 0;
  height: 2px;
  background-color: rgb(61,61,61);
  transition: width 0.6s cubic-bezier(0.25, 1, 0.5, 1);
}

@media (hover: hover) and (pointer: fine) {
  .underline:hover::before{
    left: 0;
    right: auto;
    width: 100%;
  }
}
</style>
<script setup>

</script>

<template>
    <div>
        <button class="start_btn">
            <slot></slot>
        </button>
    </div>
</template>

<script>
export default {
    name: "MyButton"
}
</script>

<style scoped lang="scss">

.start_btn {
  color: white;
  background-color: rgba(0, 0, 0, 0.3);
  max-width: 250px;
  border-width: 2px;
  padding: 5px 10px;
  border-style: solid;
  border-image: linear-gradient(35deg, rgba(255,255,255,1) 0%, rgba(46,25,204,1) 10%, rgba(0,212,255,0) 50%, rgba(32,50,215,1) 90%, rgba(255,255,255,1) 100%) 1;
}

@media (max-width: 345px) {
  .start_btn {
    padding: 5px;
	max-width: 300px;
	margin-bottom: 30px;
  }

}
</style>
<script setup>
const props = defineProps({
    id: Number,
    top_text: String,
    main_text: String,
    bottom_text: String
});
</script>

<template>
    <div class="win-btn" @mousemove.stop="move" @mouseleave.stop="mouseleave" :id="props.id">
        <div class="inner w-fit">{{ props.top_text }}</div>
        <div class="inner
             w-fit
             font-extrabold
             text-5xl
             [@media(max-width:425px)]:text-2xl
             [@media(max-width:282px)]:text-sm
                    ">
            {{ props.main_text }}
        </div>
        <div class="inner w-fit ">{{ props.bottom_text }}</div>
    </div>
</template>

<script>

export default {
    name: "Tile",
    methods: {
        mouseleave(e) {
            e.target.style.background = "#D3D3D30A";
            e.target.style.borderImage = null;
        },
        move(e) {
            if (!e.target.classList.contains('inner')) {

                const rect = e.target.getBoundingClientRect();
                const x = e.clientX - rect.left; //x position within the element.
                const y = e.clientY - rect.top; //y position within the element.
                e.target.style.background = `radial-gradient(circle at ${x}px ${y}px , rgba(255,255,255,0.2),rgba(255,255,255,0) )`;
                e.target.style.borderImage = `radial-gradient(20% 75% at ${x}px ${y}px ,rgba(255,255,255,0.7),rgba(255,255,255,0.1) ) 1 / 1px / 0px stretch `;
            } else {
                const rect = e.target.parentNode.getBoundingClientRect();
                const x = e.clientX - rect.left; //x position within the element.
                const y = e.clientY - rect.top; //y position within the element.
                e.target.parentNode.style.background = `radial-gradient(circle at ${x}px ${y}px , rgba(255,255,255,0.2),rgba(255,255,255,0) )`;
                e.target.parentNode.style.borderImage = `radial-gradient(20% 75% at ${x}px ${y}px ,rgba(255,255,255,0.7),rgba(255,255,255,0.1) ) 1 / 1px / 0px stretch `;
            }
        }
    }
}
</script>

<style scoped lang="scss">

.inner {
  z-index: -10;
}

* {
  box-sizing: border-box;
}

.win-btn {
  padding: 2rem;
  text-align: center;
  border-radius: 0px;
  background: rgba(211, 211, 211, 0.04);
  color: white;
  border: 1px solid transparent;
  z-index: 4;
  width: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  &div {
    background: transparent !important;
    border-width: 0 !important;
  }
}

button:focus {
  outline: none;
}


@media (max-width: 425px) {
  .win-btn {
    padding: 10px;
      *{
          font-weight: lighter;
      }
      max-width: 130px;
  }
}

@media (max-width: 282px) {
    .win-btn {
        padding: 10px;
        *{
            font-weight: lighter;
        }
        max-width: 130px;
    }
}

</style>
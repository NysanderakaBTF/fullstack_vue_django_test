<template>
    <div class="mt-0 min-w-full navbar-bg flex">
        <div class="min-w-full flex justify-center">
            <nav class="
            w-full
            md:px-5
            lg:px-15
            xl:px-32
            2xl:px-44
                    flex-row
                    [@media(min-width:962px)]:flex
           justify-between 
        ">
                <div class="flex items-center justify-between">
                    <img src="../assets/logo2.png" class="logo max-h-fit">
                    <!-- Mobile menu button -->
                    <div @click="showMenu = !showMenu" class="flex burger justify-end">
                        <button type="button" class="
                text-gray-400
                hover:text-gray-400
                focus:outline-none focus:text-gray-400
                
              ">
                            <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                                <path fill-rule="evenodd"
                                    d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z">
                                </path>
                            </svg>
                        </button>
                    </div>
                </div>


                <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
                <ul :class="showMenu ? 'flex' : 'hidden'" class="
                burger
            flex-grow
                w-full
                m-0
                py-5
            mt-8
            flex-col
            items-center
            justify-end
            md:gap-x-5
            lg:gap-x-7
            xl:gap-x-15
            md:mt-0
            [@media(max-width:961px)]:space-y-6
          ">
                    <!--          <li class="text-sm font-bold text-gray-800 hover:text-blue-400">-->
                    <!--            Home-->
                    <!--          </li>-->
                    <Link v-for="i in links" :key="i.id" :name="i.name" :link="i.url" />
                </ul>
            </nav>
        </div>
    </div>
</template>
<script>
import axios from "axios";
import Link from "@/components/UI/Link.vue";

export default {
    components: { Link },
    data() {
        return {
            showMenu: false,
            links: [],
        };
    },
    beforeMount() {


        axios.get('http://46.161.49.152:8000/info/links/')
            .then(value => this.links = value.data)
            .catch(reason => console.error(reason));
    }
};
</script>


<style scoped>
.navbar-bg {
    background-color: rgba(6, 8, 17, 0.3);
}

@media (max-width: 961px) {
    div.burger {
        width: 100%;
    }
    ul.burger {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        backdrop-filter: blur(4px);
        z-index: 2;
        font-size: larger;
    }
}

@media (min-width: 962px) {
    div.burger {
        visibility: hidden;
    }

    ul.burger {
        display: flex !important;
        flex-direction: row;
    }

}

@media (max-width: 400px) {
    .logo{
        max-width: 50%;
    }
    ul.burger{
        margin-top: 10px;
    }
}

</style>
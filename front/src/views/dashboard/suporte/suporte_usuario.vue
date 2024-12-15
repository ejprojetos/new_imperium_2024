<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <router-link to="/dashboard/suporte/escolher-perfil">
                    <h2 class="text-xl font-light text-[#00428F] hover:text-gray-800 transition duration-300 ease-in-out font-montserrat">
                        < Suporte</h2>
            </router-link>,
            <div class="ml-[112px]">
                <h1 class="font-montserrat text-[#00428F] text-[40px] font-bold">What is Lorem Ipsum?</h1>

                <h2 class="font-montserrat text-xl font-light">06/10/2024</h2>

                <div class="bg-white w-[713px] pt-[56px] pl-[51.5px] pr-[69.5px] pb-[58px]">
                    <p class="font-montserrat text-base">
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                    </p>

                    <img class="mt-5 mb-5" src="../../../assets/images/rectangle.png" alt="">

                    <p class="font-montserrat text-base">
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." 
                    </p>

                    <div class="w-100% bg-black h-[1px] mt-5"></div>

                    <div class="flex mt-5 gap-2.5 justify-center">
                        <span class="border-solid border-2 border-black w-[86px] h-[33px] rounded-xl flex items-center justify-center">
                            #Tag01
                        </span>
                        <span class="border-solid border-2 border-black w-[86px] h-[33px] rounded-xl flex items-center justify-center">
                            #Tag02
                        </span>
                        <span class="border-solid border-2 border-black w-[86px] h-[33px] rounded-xl flex items-center justify-center">
                            #Tag03
                        </span>
                    </div>
                </div>
            </div>

        </div>
    </LayoutDashboard>
</template>
<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';


</script>
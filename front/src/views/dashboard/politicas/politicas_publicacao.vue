<template>
 <LayoutDashboard>
    <div class="ml-[37px] mt-[54px]">
        <div class="flex gap-3">
                <router-link to="/dashboard/politicas/politicas">
                    <h2 class="text-xl font-light text-[#00428F] hover:text-gray-800 transition duration-300 ease-in-out font-montserrat">
                        < Politicas</h2>
                </router-link>
            </div>
            <div class="ml-[112px] mt-[27px]">
                <h1 class="font-montserrat text-[#00428F] font-bold text-[2.5rem]">What is Lorem Ipsum?</h1>
                <div class="mt-[66px] w-[713px] h-[651px] bg-white pt-[56px] pl-[40px] pr-[46px]">

                    <div class=" font-montserrat text-[0.938rem] text-left space-y-3 leading-4	">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        
                    </div>
                    <button class="mt-[40px] w-[96px] h-[33px] rounded-m bg-[#26438B] text-white rounded-xl font-montserrat text-xs font-medium ">Imprimir</button>
                </div>
            </div>

    </div>
 </LayoutDashboard>
</template>
<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';

</script>
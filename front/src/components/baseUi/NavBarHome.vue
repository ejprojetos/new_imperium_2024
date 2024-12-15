<template>
    <nav class="bg-white w-full z-50 relative">
        <div
            class="container mx-auto px-4 px-[50px] flex justify-between items-center h-[95px] relative fixed top-0 z-50">
            <router-link to="/">
                <img class="w-[203px]" src="../../assets/logo-institucional.svg" alt="logo">
            </router-link>

            <div class="flex items-center space-x-6 ">
                <a class="font-openSans text-lg text-[#010424] hover:text-[#00428F] cursor-pointer"
                    @click="navigateTo('inicio')">Início</a>
                <a class="font-openSans text-lg text-[#010424] hover:text-[#00428F] cursor-pointer"
                    @click="navigateTo('fluxo-de-trabalho')">Fluxo de Trabalho</a>
                <a class="font-openSans text-lg text-[#010424] hover:text-[#00428F] cursor-pointer"
                    @click="navigateTo('features')">Features</a>
                <a class="font-openSans text-lg text-[#010424] hover:text-[#00428F] cursor-pointer"
                    @click="navigateTo('depoimentos')">Depoimentos</a>
                <a class="font-openSans text-lg text-[#010424] hover:text-[#00428F] cursor-pointer"
                    @click="navigateTo('contato')">Contato</a>
                <button class="bg-[#00428F] text-white w-[119px] h-[41px] rounded-md">
                    Login
                </button>
            </div>

        </div>
        <ul>
            <li>
                <a href=""></a>
            </li>
        </ul>
    </nav>
</template>
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router';
const router = useRouter();
const route = useRoute();

const navigateTo = (sectionId: string) => {
    if (route.name === 'home') {
        const section = document.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' })
        }
    } else {
        router.push({ name: 'home', hash: `#${sectionId}` });
    }
}
</script>


<style scoped></style>
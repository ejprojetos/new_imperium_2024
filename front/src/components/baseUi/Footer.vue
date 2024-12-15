<template>
    <footer class="flex h-[316px] flex-col relative z-50 bg-white">
        <div class="flex flex-row items-center justify-around h-[256px] ">
            <div class="flex items-center">
                <img src="../../assets/logo-footer.svg" alt="logo-institucional" class="w-[300px]">
            </div>
            <div class="flex flex-col justify-items-start w-[186px] h-[192px]">
                <p class="font-montserrat text-lg font-bold mb-3">Menu</p>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm cursor-pointer"
                    @click="navigateTo('inicio')">Início</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm cursor-pointer"
                    @click="navigateTo('fluxo-de-trabalho')">Fluxo de Trabalho</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm cursor-pointer"
                    @click="navigateTo('features')">Features</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm cursor-pointer"
                    @click="navigateTo('depoimentos')">Depoimentos</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm cursor-pointer"
                    @click="navigateTo('contato')">Contato</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm cursor-pointer"
                    href="#login">Login</a>
            </div>
            <div class="flex flex-col items-start w-[186px] h-[192px]">
                <p class="font-montserrat text-lg font-bold mb-3">Ajuda</p>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm" href="">Suporte</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm" href="">Contatos</a>
                <a class="font-montserrat text-lg font-medium hover:font-bold text-sm " href="">Politicas</a>
            </div>
        </div>
        <hr class="bg-[#E5E5E5] h-1">
        <div class="w-full flex items-center justify-center h-[60px]">
            <p class="font-montserrat font-normal flex text-[#010424] ">Imperium © 2019 | Desenvolvido pela
                <span class="flex font-semibold">
                    <img class="ml-3 mr-3" src="../../assets/logo-eject.svg" alt="">
                    EJECT.
                </span>
            </p>
        </div>
    </footer>
</template>

<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router';
import { nextTick } from 'vue';  // para atrasar a rolagem


const router = useRouter();
const route = useRoute();

const navigateTo = (sectionId: string) => {
    if (route.name === 'home') {
        const section = document.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
    } else {
        router.push({ name: 'home', hash: `#${sectionId}` }).then(() => {
            nextTick(() => {
                const section = document.getElementById(sectionId);
                if (section) {
                    section.scrollIntoView({ behavior: 'smooth', block: 'start' })
                }
            })
        })
    }
}
</script>

<style scoped></style>
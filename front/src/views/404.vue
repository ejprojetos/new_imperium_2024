<template>
    <ion-page>
        <ion-content class="ion-padding">
            <div class="not-found-container">
                <div class="h-[63px] w-[100%] pl-[80px]" style="box-shadow: 0px 4px 4px 0px #00000040;">
                    <router-link to="/">
                        <div>
                            <img src="../assets/logo.svg" alt="" class="w-[58px]">
                        </div>
                    </router-link>
                </div>
                <div class="mt-[115px] w-[100%] flex flex-col items-center pb-[87px]" style="box-shadow: 0px 4px 4px 0px #00000040;">
                    <img src="../assets/images/pagina-nao-encontrada.png" alt="erro404" class="w-[332px] h-[312px]">
                    <h1 class="text-[2.688rem] mt-[30px] font-raleway font-bold	">Página não encontrada!</h1>
                    <RouterLink class="mt-4" to="/dashboard">
                        <button class="bg-[#00428F] text-white w-[104px] !h-[42px] border-none rounded-md text-lg font-openSans mt-[30px]">Voltar</button>
                    </RouterLink>
                </div>
            
            </div>
            <Footer/>
        </ion-content>
    </ion-page>

</template>
<script setup lang="ts">
import { RouterLink } from 'vue-router'
import Footer from '@/components/baseUi/Footer.vue';
</script>

<style scoped>
.not-found-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    text-align: center;
}
</style>
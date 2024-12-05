<template>
    <LayoutDashboard>
        <div class="ml-[37px] mt-[54px]">
            <div class="flex gap-3">
                <router-link to="/dashboard/suporte/escolher-perfil">
                    <h2 class="text-xl font-light text-[#00428F] hover:text-gray-800 transition duration-300 ease-in-out font-montserrat">
                        < Suporte ao usuário</h2>
                </router-link>
                <router-link to="/dashboard/suporte/faq">
                    <h2 class="text-xl font-light text-[#00428F] hover:text-gray-800 transition duration-300 ease-in-out font-montserrat">
                        < FAQ</h2>
                </router-link>
            </div>
            <div class="mt-[48px] flex w-[978px] h-[40px] bg-[#E2EAF6] rounded-full items-center justify-center">
                <h3 class="text-xl	">FAQ</h3>
                <input type="text" placeholder="Buscar" class="placeholder:text-[#00428F] text-xs placeholder:text-xs w-[673px] h-[23px] rounded-full pl-4 py-auto ml-[13px] bg-[#E2EAF6] border-2 border-DeepBlue">
                <img src="../../../assets/icons/lupa.svg" alt="" class="w-[19px] ml-[16px]">
                <button class="bg-[#00428F] text-xs text-white w-[101px] h-[23px] rounded-full ml-[12px]">Adicionar</button>
            </div>
            <div class="ml-[15px] mt-[22px] w-[898px] h-[651px] flex flex-col justify-center pl-[18px] pt-[11px] pr-[20px]" style="box-shadow: 0px 4px 4px 0px #00000040;">
                <ul class="gap-y-4 flex flex-col h-[558px]">
                    <li 
                    v-for="(item, index) in paginatedItems" :key="index"
                    class="flex w-[860px] h-[66px] items-center rounded-xl" style="box-shadow: 0px 4px 4px 0px #00000040;">
                        <p class="font-montserrat text-[0.625rem] text-[#CCCCCC] h-[50px] flex items-center border-l border-[#71C285] border-l-4 pl-[10px]">{{item.date}}</p>
                        <div class="h-[36px] w-[1px] bg-[#CCCCCC] ml-[18px]"></div>
                        <h3 class="font-montserrat font-medium text-3xl ml-[18px] w-[657px]">{{ item.title }}</h3>
                        <button class="bg-[#6CA6D0] w-[79px] h-[23px] rounded-xl text-white flex items-center justify-center">Editar</button>
                    </li>
                </ul>

                <!-- Navegação -->
                 <div class="flex justify-center mt-4 space-x-2 bg-[#E2EAF6] rounded-full">
                    <button 
                    @click="prevPage"
                    class="text-[#00428F] font-bold"
                    ><img src="../../../assets/icons/arrow-left.svg" alt="" class="h-[8px]"></button>
                    <button
                    v-for="page in totalPages"
                    :key="page"
                    @click="currentPage = page"
                    class="px-1 py-2 rounded-full text-[#00428F] text-xs transition duration-30 font-medium"
                    :class="{ 'font-bold': page === currentPage }"
                    >{{ page }}</button>
                    <button
                    @click="nextPage"
                    class="font-medium"
                    > <img src="../../../assets/icons/arrow-right.svg" alt="" class="h-[8px]"> </button>
                 </div>
                
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';
import {computed, ref} from 'vue'


const items = [
  { title: 'Título 1', date: '2024-10-30' },
  { title: 'Título 2', date: '2024-10-31' },
  { title: 'Título 3', date: '2024-11-01' },
  { title: 'Título 4', date: '2024-11-02' },
  { title: 'Título 5', date: '2024-11-03' },
  { title: 'Título 6', date: '2024-11-04' },
  { title: 'Título 7', date: '2024-11-05' },
  { title: 'Título 8', date: '2024-11-06' },
  { title: 'Título 9', date: '2024-11-07' },
  { title: 'Título 10', date: '2024-11-08' },
  { title: 'Título 11', date: '2024-11-09' },
  { title: 'Título 12', date: '2024-11-10' }
];


const currentPage = ref(1);
const itemsPage = 7;

const totalPages = computed(() => Math.ceil(items.length / itemsPage))

const paginatedItems = computed(() =>{
    const start = (currentPage.value - 1)* itemsPage;
    const end = start + itemsPage;
    return items.slice(start,end);
})

const prevPage = () =>{
    if(currentPage.value > 1){
        currentPage.value--
    }
}

const nextPage = () =>{
    if(currentPage.value < totalPages.value){
        currentPage.value++
    }
}
</script>

<style></style>
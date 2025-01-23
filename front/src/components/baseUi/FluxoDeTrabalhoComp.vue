<template>
     <section class="fluxo-de-trabalho" style="scroll-margin-top: 95px;">
        <div class="flex justify-center">
            <h2 class="font-montserrat text-4xl mt-[60px]">Fluxo de Trabalho</h2>
        </div>
        <div class="flex items-center justify-center">
            <div class="grid grid grid-cols-[323px_272px_272px_272px] gap- mt-[90px] relative">
                <img class="absolute w-[350px] h-[300px] left-[145px] top-[30px]" src="../../assets/vector-curve-line.svg" alt="">
                <img class="absolute w-[350px] h-[300px] left-[410px] top-[30px] " src="../../assets/vector-curve-line-right.svg" alt="">
                <img class="absolute w-[350px] h-[300px] left-[680px] top-[30px]" src="../../assets/vector-curve-line.svg" alt="">
                

                <!-- fluxo 1 -->
                 
                <div class="flex flex-col items-center">
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center z-10">
                        <img :src="imagem1" alt="">
                    </div>
                    <div>
                        <h3 class="font-montserrat text-2xl text-center mt-[10px] text-[#010424]">{{ titulo1 }}</h3>
                        <p class="text-center w-[323px] font-montserrat text-lg	text-[#010424]">{{descricao1}}</p>
                    </div>
                </div>

                <!-- fluxo 2 -->

                <div class="h-full flex flex-col items-center z-10 ">
                    <div class="">
                        <h3 class="font-montserrat text-2xl text-center w-[222px] text-[#010424] ">{{titulo2}}</h3>
                        <p class="text-center font-montserrat text-lg text-[#010424] w-[222px] h-[150px]">{{descricao2}}</p>
                    </div>
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center mt-5">
                        <img :src="imagem2" alt="">
                    </div>
                </div>

                <!-- fluxo 3 -->

                <div class="flex flex-col items-center z-10">
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center">
                        <img :src="imagem3" alt="">
                    </div>
                    <div class="w-[222px]">
                        <h3 class="font-montserrat text-2xl text-center mt-3 text-[#010424]">{{titulo3}}</h3>
                        <p class="text-center font-montserrat text-lg	text-[#010424]">{{descricao3}}</p>
                    </div>
                </div>

                <!-- fluxo 4 -->
                <div class="flex flex-col items-center z-10">
                    <div class="w-[222px]">
                        <h3 class="font-montserrat text-2xl text-center">{{titulo4}}</h3>
                        <p class="text-center font-montserrat text-lg mt-3 text-[#010424] h-[150px]">{{descricao4}}</p>
                    </div>
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center mt-5">
                        <img :src="imagem4" alt="">
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { useFluxoStore } from '@/stores/institucional/fluxo.store';
import { onMounted, ref } from 'vue';


const fluxoStore = useFluxoStore();


//dados do fluxo
const titulo1 = ref('');
const descricao1 = ref('');
const imagem1 = ref<string | undefined>(undefined);
const titulo2 = ref('');
const descricao2 = ref('');
const imagem2 = ref<string | undefined>(undefined);
const titulo3 = ref('');
const descricao3 = ref('');
const imagem3 = ref<string | undefined>(undefined);
const titulo4 = ref('');
const descricao4 = ref('');
const imagem4 = ref<string | undefined>(undefined);

//carregar dados do fluxo
onMounted( async() => {
    await fluxoStore.fetchFluxo()
    if(fluxoStore.fluxo && fluxoStore.fluxo.length > 0){
        titulo1.value = fluxoStore.fluxo[0].titulo1;
        descricao1.value = fluxoStore.fluxo[0].descricao1;
        imagem1.value = fluxoStore.fluxo[0].imagem1;
        titulo2.value = fluxoStore.fluxo[0].titulo2;
        descricao2.value = fluxoStore.fluxo[0].descricao2;
        imagem2.value = fluxoStore.fluxo[0].imagem2;
        titulo3.value = fluxoStore.fluxo[0].titulo3;
        descricao3.value = fluxoStore.fluxo[0].descricao3;
        imagem3.value = fluxoStore.fluxo[0].imagem3;
        titulo4.value = fluxoStore.fluxo[0].titulo4;
        descricao4.value = fluxoStore.fluxo[0].descricao4;
        imagem4.value = fluxoStore.fluxo[0].imagem4;

    } else {
        console.error('Erro ao buscar dados do fluxo');
    }
})

</script>
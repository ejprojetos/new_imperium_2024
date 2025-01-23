<template>
<section class="h-[875px] bg-[#F5F9FA] flex flex-col items-center"  id="features" style="scroll-margin-top: 95px;">
        <div class="max-w-screen-lg flex flex-col items-center">
            <img src="../../assets/rectangle-features.svg">
            <h2 class="font-montserrat text-4xl mt-[60px]">Features</h2>
        </div>
        <div class="flex gap-[40px] flex-wrap justify-center w-[1200px] mt-[90px]">

            <!-- Feature 1 -->
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img :src="imagem1" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">{{titulo1}}</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">{{descricao1}}</p>
            </div>

            <!-- Feature 2 -->
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img :src="imagem2" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">{{titulo2}}</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">{{descricao2}}</p>
            </div>

            <!-- Feature 3 -->
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img :src="imagem3" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">{{titulo3}}</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">{{descricao3}}</p>
            </div>

            <!-- Feature 4 -->
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img :src="imagem4" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">{{titulo4}}</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">{{descricao4}}</p>
            </div>

            <!-- Feature 5 -->
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img :src="imagem5" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">{{titulo5}}</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">{{descricao5}}</p>
            </div>
        </div>
        <div class="max-w-screen-lg flex flex-col items-center mt-[73px]">
            <img src="../../assets/rectangle-features.svg">
        </div>
    </section>
</template>

<script setup lang="ts">
import { useFeatureStore } from '@/stores/institucional/feature.store';
import { onMounted, ref } from 'vue';

const featureSetore = useFeatureStore();


//dados do Feature
const titulo1 = ref('');
const descricao1 = ref('');
const imagem1 = ref<string | undefined>(undefined);
const titulo2 = ref('');
const descricao2 = ref('');
const imagem2 = ref<string | undefined>(undefined);
const titulo3 = ref('');
const descricao3 = ref<string | undefined>(undefined);
const imagem3 = ref<string | undefined>(undefined);
const titulo4 = ref('');
const descricao4 = ref<string | undefined>(undefined);
const imagem4 = ref<string | undefined>(undefined);
const titulo5 = ref('');
const descricao5 = ref<string | undefined>(undefined);
const imagem5 = ref<string | undefined>(undefined);

//carregar dados
onMounted( async () =>{
    await featureSetore.fetchFeature()
    if(featureSetore.features && featureSetore.features.length > 0){
        titulo1.value = featureSetore.features[0].titulo1;
        descricao1.value = featureSetore.features[0].descricao1;
        imagem1.value = featureSetore.features[0].imagem1;
        titulo2.value = featureSetore.features[0].titulo2;
        descricao2.value = featureSetore.features[0].descricao2;
        imagem2.value = featureSetore.features[0].imagem2;
        titulo3.value = featureSetore.features[0].titulo3;
        descricao3.value = featureSetore.features[0].descricao3;
        imagem3.value = featureSetore.features[0].imagem3;
        titulo4.value = featureSetore.features[0].titulo4;
        descricao4.value = featureSetore.features[0].descricao4;
        imagem4.value = featureSetore.features[0].imagem4;
        titulo5.value = featureSetore.features[0].titulo5;
        descricao5.value = featureSetore.features[0].descricao5;
        imagem5.value = featureSetore.features[0].imagem5;
    } else {
        console.error('Erro ao buscar dados iniciais');
        titulo1.value = "testo caso não encontrado"
    }
})



</script>
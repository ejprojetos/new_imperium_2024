<template>
    <section class="banner" id="inicio">
        <div class="flex justify-between items-center banner h-[655px] bg-cover bg-center bg-no-repeat" :style="{ backgroundImage: `url(${imagem})` }">
            <div class="flex flex-col items-start ml-[130px]">
                <!-- <h1 class="font-arboria text-[3.125rem] w-[732px]  text-white leading-tight	">Praesent est mi, consequat sed aliquam in, ornare quis neque Integer.</h1> -->

                <h1 class="font-arboria text-[3.125rem] w-[732px]  text-white leading-tight	">{{ frase }}</h1>
                
                <button class="bg-[#00428F] text-white w-[182px] h-[41px] rounded-md mt-10">
                    Fale conosco
                </button>
            </div>
            <div class="flex items-center px-4 relative top-[250px] right-[40px] bg-[#E1E7EF] w-[68px] h-[68px] rounded-full cursor-pointer" style="box-shadow: 0px 4px 4px 0px #02063640;">
                <font-awesome-icon icon="envelope" class="text-blue-500 text-[35px] text-[#00428F]" />
            </div>
        </div>  
    </section>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { useInicialStore } from '@/stores/institucional/inicial.store';

const inicialStore = useInicialStore();
const frase = ref('');
const imagem = ref<string | File | null>(null);

onMounted(async () => {

await inicialStore.fetchInicial()
if(inicialStore.inicial && inicialStore.inicial.length > 0){
    frase.value = inicialStore.inicial[0].frase;
    imagem.value = inicialStore.inicial[0].imagem;
} else {
    console.error('Erro ao buscar dados iniciais');
    frase.value = "testo caso não encontrado"
}
frase.value = inicialStore.inicial[0].frase;
imagem.value = inicialStore.inicial[0].imagem;
})

</script>
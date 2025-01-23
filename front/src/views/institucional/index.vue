<template>
    <NavBarHome class="fixed top-0 left-0 w-full z-50 bg-white"/>
    
    
    <!-- Banner Inicial -->
    <Banner/>
    

    <!-- Fluxo de Trabalho -->
    <FluxoDeTrabalhoComp/>
    

    <!-- Features -->
    <FeaturesComponent/>

      
    <!-- Depoimentos -->
    <section class="h-[611px] bg-[#DEECFA] pt-[70px]" id="depoimentos" style="scroll-margin-top: 95px;">
        <div class="flex justify-center">
            <h2 class="font-montserrat text-4xl">Depoimentos</h2>
        </div>
        <CarroselInstitucional/>
        <div class="flex flex-col items-center mt-[15px]">
            <img src="../../assets/rectangle-features.svg">
        </div>
    </section>

    <!-- Contato -->

    <section class="contato h-[839px] pt-[91px] flex flex-col items-center" id="contato" style="scroll-margin-top: 95px;">
        <div class="flex justify-center">
            <h2 class="font-montserrat text-4xl">Contato</h2>
        </div>
        <form @submit.prevent="submitForm" class="w-[634px] mt-[60px]">
                    <h2 class="mb-4 text-xl font-montserrat text-black font-bold">Identificação do paciente:</h2>
                    
                    <div class="grid grid-cols-1 gap-4">
                        <div>
                            <label class="block mb-2 text-base font-montserrat labelText text-[#010424] ">
                                Nome:
                            </label>
                            <input 
                            v-model="FormData.nome"
                            type="text"
                            class="w-full px-2 py-1 border border-[#00428F] rounded-lg"
                            />
                        </div>
                    </div>
                    
                    <div>
                        <label class="block mt-[15px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Celular:
                        </label>
                        <input 
                        v-model="FormData.telefone"
                        type="tel"
                        class="w-full px-2 py-1 border border-[#00428F] rounded-lg "
                        />
                    </div>
                    <div>
                        <label class="block mt-[15px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Email:
                        </label>
                        <input 
                        v-model="FormData.email"
                        type="email"
                        class="w-full px-2 py-1 border border-[#00428F] rounded-lg"
                        />
                    </div>
                    <div>
                        <label class="block mt-[15px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Assunto:
                        </label>
                        <input 
                        v-model="FormData.assunto"
                        type="text"
                        class="w-full px-2 py-1 border border-[#00428F] rounded-lg "
                        />
                    </div>
                    <div>
                        <label class="block mt-[15px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Mensagem:
                        </label>
                        <textarea 
                        v-model="FormData.mensagem"
                        type="email"
                        class="w-full h-[146px] px-2 py-1 border border-[#00428F] rounded-lg"
                        style="resize:none"/>
                    </div>

                    <button  class="w-full px-2 py-1 border border-[#00428F] rounded-lg bg-[#00428F] text-[#FAFAFA] mt-[45px] transition-transform transform active:scale-95 focus:outline-none" style="box-shadow: 0px 4px 4px 0px #00000040; ">Enviar</button>
                </form>
    </section>



    <Footer/>
</template>

<script setup lang="ts">
defineOptions({
  name: 'InstitucionalIndex'
});
import NavBarHome from '@/components/baseUi/NavBarHome.vue';
import Banner from '@/components/baseUi/Banner.vue';
import FluxoDeTrabalhoComp from '@/components/baseUi/FluxoDeTrabalhoComp.vue';
import Footer from '@/components/baseUi/Footer.vue';
import CarroselInstitucional from '@/components/baseUi/CarroselInstitucional.vue';

import { toast } from 'vue-sonner';
import type { Contato } from '@/types/institucional.types';
import FeaturesComponent from '@/components/baseUi/FeaturesComponent.vue';
import { reactive } from 'vue';
import { useContatoStore } from '@/stores/contato/contato.store';


const contatoStore = useContatoStore()


const FormData = reactive<Contato>({
    id: '',
    nome: '',
    telefone: '',
    email: '',
    assunto:'',
    mensagem: '',
    respondido: false,
    envio_data:'',
    respondido_data: new Date().toISOString().split('T')[0]
})



const submitForm = async () => {
    try{
        await contatoStore.creatContato(FormData);
        toast.success('Formulário enviado com sucesso!');
        resetForm()
    } catch (error){
        console.error('Erro ao enviar formulário:', error);
        toast.error('Ocorreu um erro ao enviar o formulário.')
    }
}

const resetForm =() => {
    FormData.nome = '';
    FormData.telefone = '';
    FormData.email = '';
    FormData.mensagem = '';
    FormData.assunto = '';
    
}
</script>

<style scoped>

    .contato{
        background-image: url('../../assets/images/bg-contato.jpg');
    }
</style>

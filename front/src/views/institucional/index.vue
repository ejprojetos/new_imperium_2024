<template>
    <NavBarHome class="fixed top-0 left-0 w-full z-50 bg-white"/>

    <section class="banner" id="inicio">
        <div class="flex justify-between items-center banner h-[655px] bg-cover bg-center bg-no-repeat">
            <div class="flex flex-col items-start ml-[130px]">
                <h1 class="font-arboria text-[3.125rem] w-[732px]  text-white leading-tight	">Praesent est mi, consequat sed aliquam in, ornare quis neque Integer.</h1>
                <button class="bg-[#00428F] text-white w-[182px] h-[41px] rounded-md mt-10">
                    Fale conosco
                </button>
            </div>
            <div class="flex items-center px-4 relative top-[250px] right-[40px] bg-[#E1E7EF] w-[68px] h-[68px] rounded-full cursor-pointer" style="box-shadow: 0px 4px 4px 0px #02063640;">
                <font-awesome-icon icon="envelope" class="text-blue-500 text-[35px] text-[#00428F]" />
            </div>
        </div>  
    </section>

    <!-- Fluxo de Trabalho -->

    <section class="fluxo-de-trabalho h-[676px] bg-[#F5F9FA] flex flex-col" id="fluxo-de-trabalho" style="scroll-margin-top: 95px;">
        <div class="flex justify-center">
            <h2 class="font-montserrat text-4xl mt-[60px]">Fluxo de Trabalho</h2>
        </div>
        <div class="flex items-center justify-center">
            <div class="grid grid grid-cols-[323px_272px_272px_272px] gap- mt-[90px] relative">
                <img class="absolute w-[350px] h-[300px] left-[145px] top-[30px]" src="../../assets/vector-curve-line.svg" alt="">
                <img class="absolute w-[350px] h-[300px] left-[410px] top-[30px] " src="../../assets/vector-curve-line-right.svg" alt="">
                <img class="absolute w-[350px] h-[300px] left-[680px] top-[30px]" src="../../assets/vector-curve-line.svg" alt="">
                <div class="flex flex-col items-center">
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center z-10">
                        <img src="../../assets/icons/icone-formulario.svg" alt="">
                    </div>
                    <div>
                        <h3 class="font-montserrat text-2xl text-center mt-[10px] text-[#010424]">Preencher Formulário</h3>
                        <p class="text-center w-[323px] font-montserrat text-lg	text-[#010424]">Est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie</p>
                    </div>
                </div>
                <div class="h-full flex flex-col items-center z-10 ">
                    <div class="">
                        <h3 class="font-montserrat text-2xl text-center w-[222px] text-[#010424] ">Validação de Boleto</h3>
                        <p class="text-center font-montserrat text-lg text-[#010424] w-[222px]">Est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie</p>
                    </div>
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center mt-5">
                        <img src="../../assets/icons/icone-validacao.svg" alt="">
                    </div>
                </div>
                <div class="flex flex-col items-center z-10">
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center">
                        <img src="../../assets/icons/icone-emissao.svg" alt="">
                    </div>
                    <div class="w-[222px]">
                        <h3 class="font-montserrat text-2xl text-center mt-3 text-[#010424]">Emissão de Boleto</h3>
                        <p class="text-center font-montserrat text-lg	text-[#010424]">Est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie</p>
                    </div>
                </div>
                <div class="flex flex-col items-center z-10">
                    <div class="w-[222px]">
                        <h3 class="font-montserrat text-2xl text-center">Minha Gestão descomplicada</h3>
                        <p class="text-center font-montserrat text-lg mt-3 text-[#010424]">Est mi, consequat sed aliquam in, ornare quis neque. Integer euismod libero eu nibh blandit molestie</p>
                    </div>
                    <div class="h-[150px] w-[150px] bg-[#DEECFA] rounded-full flex items-center justify-center mt-5">
                        <img src="../../assets/icons/icone-descomplicado.svg" alt="">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Features -->
    <section class="h-[875px] bg-[#F5F9FA] flex flex-col items-center" id="features" style="scroll-margin-top: 95px;">
        <div class="max-w-screen-lg flex flex-col items-center">
            <img src="../../assets/rectangle-features.svg">
            <h2 class="font-montserrat text-4xl mt-[60px]">Features</h2>
        </div>
        <div class="flex gap-[40px] flex-wrap justify-center w-[1200px] mt-[90px]">
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img src="../../assets/icons/icone-consultas.svg" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">Gestão de Consultas</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">Realize todos os processos de consultas de maneira descomplicada e simplificada.</p>
            </div>
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img src="../../assets/icons/icone-financeiro.svg" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">Gestão Financeira</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">Tenha seus dados financeiros organizados de modo facilitado.</p>
            </div>
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img src="../../assets/icons/icone-prontuarios.svg" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">Prontuários</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">Para médicos, cadastre, edite, compartilhe seus prontuários, poupe trabalho e tempo.</p>
            </div>
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img src="../../assets/icons/pacientes.svg" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">Gestão de Pacientes</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">Possua conhecimento sobre a demanda de pacientes que sua clínica recebe.</p>
            </div>
            <div class="w-[289px] h-[243px] bg-[#FAFAFA] flex flex-col items-center pt-[25px] " style="box-shadow: 0px 4px 8px 0px #02063633;">
                <img src="../../assets/icons/icone-funcionarios.svg" alt="">
                <h2 class="font-roboto text-[#010424] text-[26px]">Funcionários</h2>
                <p class="font-roboto text-[18px] w-[235px] text-center">Gestão de funcionários, gerencie sua clínica da melhor forma possível.</p>
            </div>
        </div>
        <div class="max-w-screen-lg flex flex-col items-center mt-[73px]">
            <img src="../../assets/rectangle-features.svg">
        </div>
    </section>

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
                        <label class="block mt-[20px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Celular:
                        </label>
                        <input 
                        v-model="FormData.telefone"
                        type="tel"
                        class="w-full px-2 py-1 border border-[#00428F] rounded-lg "
                        />
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Email:
                        </label>
                        <input 
                        v-model="FormData.email"
                        type="email"
                        class="w-full px-2 py-1 border border-[#00428F] rounded-lg"
                        />
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-base font-montserrat br-16 text-[#010424] ">
                            Mensagem:
                        </label>
                        <textarea 
                        v-model="FormData.mensagem"
                        type="email"
                        class="w-full h-[146px] px-2 py-1 border border-[#00428F] rounded-lg"
                        />
                    </div>

                    <button  class="w-full px-2 py-1 border border-[#00428F] rounded-lg bg-[#00428F] text-[#FAFAFA] mt-[51px] transition-transform transform active:scale-95 focus:outline-none" style="box-shadow: 0px 4px 4px 0px #00000040; ">Enviar</button>
                </form>
    </section>



    <Footer/>
</template>

<script setup lang="ts">
defineOptions({
  name: 'InstitucionalIndex'
});
import NavBarHome from '@/components/baseUi/NavBarHome.vue';
import Footer from '@/components/baseUi/Footer.vue';
import CarroselInstitucional from '@/components/baseUi/CarroselInstitucional.vue';

import { reactive } from 'vue';
import { toast } from 'vue-sonner';
import { submitContato } from '@/services/contato.service'; // Adjust the path as necessary
import type { Contato } from '@/types/contato.types';


const FormData = reactive<Contato>({
    id: 0,
    nome: '',
    telefone: '',
    email: '',
    mensagem: '',
    respondido: false,
    respondido_data: new Date().toISOString().split('T')[0]
})

// const submitForm = () => {
    
//     console.log('Form submitted', FormData)
//     toast.success('Salvo com sucesso!')

// };

const submitForm = async () => {
    try{
        await submitContato(FormData);
        toast.success('Formulário enviado com sucesso!')
    } catch (error){
        console.error('Erro ao enviar formulário:', error);
        toast.error('Ocorreu um erro ao enviar o formulário.')
    }
}
</script>

<style scoped>
    .banner{
        background-image: url('../../assets/images/banner-instit.jpg');
    }
    .contato{
        background-image: url('../../assets/images/bg-contato.jpg');
    }
</style>

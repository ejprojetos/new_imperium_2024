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
            <div class="ml-[112px] mt-[27px]">
                <h1 class="font-montserrat text-[#00428F] font-bold text-[2.5rem]">Cadastrar Perguntas</h1>

                <div class="bg-white w-[669px] h-[747px] flex justify-center">
                    <form class="w-[573px] space-y-[20px] mt-[51.5px]" @submit.prevent="submitForm">
                        <div class="flex flex-col space-y-[16px]" >

                            <label for="titulo" class="font-montserrat text-2xl font-light text-black">Titulo:</label>
                            <input v-model="formData.title" type="text" id="titulo" name="titulo" 
                            class="border-2 border-black rounded-xl h-[35px] pl-[26px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	"
                            placeholder="Digite seu título" >
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="pergunta" class="font-montserrat text-2xl font-light text-black">Perguntas: </label>
                            <input v-model="formData.questions" type="text" id="pergunta" name="pergunta" placeholder="Digite a pergunta" class="border-2 border-black rounded-xl h-[35px] pl-[26px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	">
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="conteudo" class="font-montserrat text-2xl font-light text-black">Conteudo:</label>
                            <textarea v-model="formData.content" name="conteudo" id="conteudo" placeholder="Digite a resposta" class="border-2 border-black rounded-xl h-[150px] resize-none pl-[26px] pt-[21px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	"></textarea>
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="perfil" class="font-montserrat text-2xl font-light text-black">Pefil:</label>
                            <select v-model="formData.profile" id="perfil" name="perfil" class="border-2 border-black rounded-xl h-[35px] pl-[26px] font-montserrat text-2xl font-light">
                                <option value="Nenhum" selected class="font-montserrat text-2xl font-light">Nenhum</option>
                                <option value="ADMIN" class="font-montserrat text-2xl font-light">Administrador</option>
                                <option value="CLINIC" class="font-montserrat text-2xl font-light">Clinica</option>
                                <option value="PATIENT" class="font-montserrat text-2xl font-light">Paciente</option>
                            </select>
                        </div>
                        <div class="flex flex-col space-y-[16px]">
                            <label for="tags" class="font-montserrat text-2xl font-light text-black">Tags:</label>
                            <input v-model="tagsInput"
                            @input="updateTags" 
                            type="text" 
                            id="tags" 
                            name="tags" 
                            placeholder="Digite as #tags" 
                            class="border-2 border-black rounded-xl h-[35px] pl-[26px] placeholder-shown:font-montaserrat placeholder-shown:text-xl	">
                        </div>
                        <div class="flex justify-between mt-[23px]">
                            <button class="w-[130px] h-[33px] rounded-m bg-[#26438B] text-white rounded-xl font-montserrat text-lg font-medium" >Cadastrar</button>
                            <button class="w-[203px] h-[33px] rounded-m bg-[#26438B] text-white rounded-xl font-montserrat text-lg font-medium" >Salvar e cadastrar</button>
                        </div>
                    </form>
                </div>
            </div>
            
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue';
import { useFaqStore } from '@/stores/ajuda/faq.store';
import type { Faq } from '@/types/ajuda.types';
import { reactive, ref } from 'vue';
import { toast } from 'vue-sonner';

const faqStore = useFaqStore();

const formData = reactive({
    title:'',
    questions: '',
    content: '',
    profile: '',
    tags: [] as { name: string }[]
})

const tagsInput = ref('')

const updateTags = () => {
    formData.tags = tagsInput.value
        .trim() //remove espaços
        .split(/\s+/) // divide por espaço em branco
        .filter(tag => tag !=='') // remove strings vazia
        .map(tag => ({name: tag}));// map to objects with id and name properties
}
const formatFaqData = async() : Promise<Faq> =>{
    return{
        title: formData.title,
        questions: formData.questions,
        content: formData.content,
        profile: formData.profile,
        tags: JSON.parse(JSON.stringify(formData.tags))
    }
}

const submitForm = async () => {
    try {
        const faqData = await formatFaqData()
        console.log(faqData)


        if(faqData.title === '' ||faqData.questions === '' || faqData.content === '' || faqData.profile === ''){
            toast('Preencha todos os campos')
            return;
        }
        
        const result = await faqStore.createFaq(faqData)
        console.log(result)

            if(result?.id){
                toast.success('Pergunta cadastrada com sucesso')
            }else{
                console.log('result: ',result)
                console.error(result)
                toast.error('Erro ao cadastrar pergunta')
            }
        }
    catch (error) {
        console.error(error)
        toast.error('Erro ao cadastrar pergunta')
    }
}


</script>
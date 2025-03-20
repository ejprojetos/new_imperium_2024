<template>
    <LayoutDashboard>
        <div class="p-1">
            <div class="flex items-center mb-6 w-full max-w-[1000px] m-6">
                <RouterLink to="/dashboard/suporte/politicas"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <span class="mr-2"></span>
                    <span>
                        < Políticas</span>
                </RouterLink>

            </div>
            <div class="flex items-center mb-6 w-full max-w-[1000px] mx-auto">
                <span class="text-[#00428F] font-montserrat text-4xl font-bold leading-none">Cadastrar</span>
            </div>


            <div class="p-10 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto">

            <form @submit.prevent="submitForm">
                <div class="grid grid-cols-1 gap-4 mb-6">

                    <label class="text-black font-montserrat text-lg font-light leading-none">Perfil:</label>

                    <select
                        class="select w-full rounded-[100px] border border-black flex h-[35px] min-h-[35px] px-7 items-center gap-[10px] self-stretch my-1"
                        v-model="formData.profile">
                        <option v-for="option in profiles" :key="option.value" :value="option.value">
                            {{ option.label }}
                        </option>
                    </select>

                </div>
                <div class="grid grid-cols-1 gap-4 mb-6">
                    <label class="text-black font-montserrat text-lg font-light leading-none">Título:</label>
                    <input type="text" class="w-full border border-black rounded-full border border-black flex h-[35px] min-h-[35px] px-7 items-center gap-[10px] self-stretch my-1" v-model="formData.title">
                </div >
                <div class="grid grid-cols-1 gap-4 mb-6">
                    <label class="text-black font-montserrat text-lg font-light leading-none">Conteúdo:</label>
                    <textarea placeholder="Digite o conteúdo"
                        class="textarea textarea-bordered textarea-lg w-full border border-black" v-model="formData.content"></textarea>
                </div>
                
                <div class="flex justify-between">
    
                    <button class="btn btn-active btn-neutral w-1/8 text-white hover:bg-blue min-h-[35px] h-[40px] px-6"
                        style="background-color: #00428F;">Cadastrar</button>
                    <button class="btn btn-active btn-neutral w-1/6 text-white p-1 hover:bg-blue min-h-[35px] h-[40px]"
                        style="background-color: #00428F;">Salvar e cadastrar</button>
                </div>
            </form>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { usePolicyStore } from '@/stores/ajuda/policys.store'
import { toast } from 'vue-sonner'

const isEditing = ref(false)
const originalData = ref<manual | null>(null)

const policyStore = usePolicyStore();

const profiles = ref([
    {label:'Administrador',value: "ADMIN"},
    {label:'Clínica', value:'CLINIC'},
    {label:'Médico', value:'DOCTOR'},
    {label:'Paciente',value:'PATIENT'},
    {label:'Recepcionista',value: 'RECEPTIONIST'}  ])


const optionSelected = ref({
    perfil: 'Médico',
})
const formData = reactive({
    profile:'',
    title:'',
    content:''
})

const formatPolicyData = async() :  Promise<Policies> =>{
    return{
        profile: formData.profile.valueOf(),
        title: formData.title,
        content: formData.content
    }
}

const submitForm = async() =>{
    try{
        const policyData = await formatPolicyData()
        console.log("Enviando os dados:", policyData)

        if(policyData.content === '' || policyData.profile === '' || policyData.title === ''){
            toast('Preencha todos os campos')
            return
        }

        const result = await policyStore.createPolicy(policyData)

        if(result?.id){
            toast.success('Política cadastrada com sucesso')
        }else{
            toast.error("Erro ao cadastrar política")
        }
    }catch(error){
        console.error(error)
        toast.error('Erro ao cadastrar pergunta')
    }
}

// function startEditing() {
//     originalData.value = JSON.parse(JSON.stringify(formData))
//     isEditing.value = true
// }

// function cancelEditing() {
//     if (originalData.value) {
//         Object.assign(formData, originalData.value)
//     }
//     isEditing.value = false
// }

// function saveChanges() {
//     console.log('Saving changes:', formData)
//     isEditing.value = false
// }
</script>

<template>
    <LayoutDashboard>
        <div class="p-1">
            <div class="flex items-center mb-6 w-full max-w-[1000px] m-6">
                <RouterLink
                    to="/dashboard/suporte/administrador"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <span class="mr-2"></span>
                    <span>< Suporte ao usuário</span>
                </RouterLink>
                <RouterLink
                    to="/dashboard/suporte/todos-manuais"
                    class="flex items-center text-blue-600 hover:text-blue-800 mb-4">
                    <span class="mr-2"></span>
                    <span>< Manuais</span>
                </RouterLink>
            </div>
            <div class="flex items-center mb-6 w-full max-w-[1000px] mx-auto">
                <span class="text-[#00428F] font-montserrat text-4xl font-bold leading-none">
                    Editar Manuais de {{ perfil }}
                </span>
            </div>

            <div class="p-10 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto">
                <div class="grid grid-cols-1 gap-4 mb-6">
                    <label class="text-black font-montserrat text-lg font-light leading-none">
                        Titulo:
                    </label>

                    <input
                        type="text"
                        class="w-full rounded-[100px] border border-black flex h-[35px] px-7 items-center gap-[10px] self-stretch my-1"
                        v-model="formData.titulo"
                        placeholder="Titulo" />
                </div>

                <div class="grid grid-cols-1 gap-4 mb-6">
                    <label class="text-black font-montserrat text-lg font-light leading-none">
                        Perfil:
                    </label>


                    <select
                        class="select w-full rounded-[100px] border border-black flex h-[35px] min-h-[35px] px-7 items-center gap-[10px] self-stretch my-1"
                        v-model="optionSelected.perfil"
                        disabled>
                        <option 
                            v-for="option in formData.perfil" 
                            :key="option.value" 
                            :value="option.value">
                            {{ option.label }}
                        </option>
                    </select>
                </div>

                <div class="relative w-full">
                    <!-- Input file invisível -->
                    <input
                        type="file"
                        class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                        @change="handleFileChange"
                        ref="fileInput" 
                        />

                    <!-- Estilização personalizada do botão -->
                    <div
                        class="flex justify-between items-center w-full h-[40px] px-4 rounded-[100px] border border-black bg-gray-100 cursor-pointer"
                        @click="triggerFileInput">
                        <span class="truncate">
                        {{ fileName || (typeof formData.manual_archive === 'string' ? extractFileName(formData.manual_archive) : 'Selecionar arquivo...') }}
                        </span>

                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 512 512"
                            class="h-5 w-5 opacity-70">
                            <path
                                d="M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1 0 32c0 8.8 7.2 16 16 16l32 0zM362.7 18.7L348.3 33.2 325.7 55.8 314.3 67.1l33.9 33.9 62.1 62.1 33.9 33.9 11.3-11.3 22.6-22.6 14.5-14.5c25-25 25-65.5 0-90.5L453.3 18.7c-25-25-65.5-25-90.5 0zm-47.4 168l-144 144c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 16.4-6.2 22.6 0s6.2 16.4 0 22.6z" />
                        </svg>
                    </div>
                </div>

                <div class="flex justify-between mt-6">
                    <button
                        @click="submitForm"
                        class="btn btn-active btn-neutral w-1/8 text-white hover:bg-blue min-h-[35px] h-[40px] px-6"
                        style="background-color: #00428f">
                        Cadastrar
                    </button>
                    <button
                        @click="submitAndRegister"
                        class="btn btn-active btn-neutral w-1/6 text-white p-1 hover:bg-blue min-h-[35px] h-[40px]"
                        style="background-color: #00428f">
                        Salvar e cadastrar
                    </button>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'
import { useManualStore } from '@/stores/ajuda/manualStore'
import { perfilSelecionado } from '@/stores/ajuda/perfilStore'
import { useUserStore } from '@/stores/user/useUserStore'
import { storeToRefs } from 'pinia'

const manualStore = useManualStore()
const isEditing = ref(false)
const route = useRoute()
const id = route.params.id as string | undefined


// const userStore = useUserStore()
// const { role } = storeToRefs(userStore)
// console.log('ROLE: ', role.value)


function extractFileName(path: string): string {
    return path.split('/').pop() || 'Selecionar arquivo...';
}



interface ManualForm {
    titulo: string
    perfil: perfilOption[]
    manual_archive: string | File | null
    creation_date?: string
}

const formData = reactive<ManualForm>({
    titulo: '',
    perfil: [
        {label:'Administrador', value:'ADMIN'},
        {label:'Paciente', value: 'PATIENT'},
        {label:'Clínica', value: 'CLINIC'},
        {label:'Médico', value: 'DOCTOR'},
        {label:'Recepcionista', value: 'RECEPTIONIST'}]
        ,
    manual_archive: null as File | null
})

const optionSelected = ref({
    perfil: perfilSelecionado.value
})
console.log('PERFIL SELECIONADO: ',perfilSelecionado.value)


onMounted( async () => {
    if(id){
        await manualStore.fetchSingleManual(id)
        console.log('MANUAL: ', manualStore.currentManual)
        formData.titulo = manualStore.currentManual?.title || ''
        optionSelected.value.perfil = manualStore.currentManual?.profile || ''
        formData.manual_archive = manualStore.currentManual?.manual_archive || ''
    }else{
        manualStore.resetCurrentManual()
    }
})



console.log('PERFIL SELECIONADO: ',perfilSelecionado.value)

const perfil = computed(() =>{
    switch(perfilSelecionado.value){
        case 'ADMIN':
            return 'Administrador'
        case 'PATIENT':
            return 'Paciente'
        case 'CLINIC':
            return 'Clínica'
        case 'DOCTOR':
            return 'Médico'
        case 'RECEPTIONIST':
            return 'Recepcionista'
        default:
            return 'Perfil não encontrado'
    }
})


const fileName = ref<string | null>(null)
const fileInput = ref<HTMLInputElement | null>(null)



function handleFileChange(event: Event) {
    const input = event.target as HTMLInputElement
    if (input.files && input.files[0]) {
        formData.manual_archive = input.files[0]
        fileName.value = input.files[0].name
    }
}

async function submitForm() {
    if(id){
        // Prepare payload with correct types for updateManual
        await manualStore.updateManual(id, {
            title: formData.titulo,
            profile: optionSelected.value.perfil,
            manual_archive: typeof formData.manual_archive === 'string' ? undefined : formData.manual_archive ?? undefined,
            creation_date: formData.creation_date
        })
        toast('Manual atualizado com sucesso!');
    }else{
    try {
        if (!formData.titulo || !formData.perfil || !formData.manual_archive) {
            toast('Preencha todos os campos');
            return;
        }

        await manualStore.createManual({
            titulo: formData.titulo,
            profile: optionSelected.value.perfil,
            manual_archive: formData.manual_archive,
            creation_date: new Date().toISOString()
        });

        toast('Manual cadastrado com sucesso!');
    } catch (error) {
        toast('Erro ao cadastrar manual');
        console.error(error);
    }
    }
}

async function submitAndRegister() {
    await submitForm();
    formData.titulo = '';
    formData.manual_archive = '';
    fileName.value = null;
}

function triggerFileInput() {
    fileInput.value?.click()
}



</script>

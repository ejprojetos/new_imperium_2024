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
                <span class="text-[#00428F] font-montserrat text-4xl font-bold leading-none">Editar Políticas</span>
            </div>


            <div class="p-10 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto">


                <div class="grid grid-cols-1 gap-4 mb-6">

                    <label class="text-black font-montserrat text-lg font-light leading-none">Perfil:</label>

                    <select
                        class="select w-full rounded-[100px] border border-black flex h-[35px] min-h-[35px] px-7 items-center gap-[10px] self-stretch my-1"
                        v-model="optionSelected.perfil">
                        <option v-for="option in formData.perfil" :key="option">
                            {{ option }}
                        </option>
                    </select>

                </div>

                <div class="grid grid-cols-1 gap-4 mb-6">
                    <label class="text-black font-montserrat text-lg font-light leading-none">Conteúdo:</label>
                    <textarea placeholder="Digite o conteúdo"
                        class="textarea textarea-bordered textarea-lg w-full border border-black"></textarea>
                </div>

                <div class="flex justify-between">

                    <button class="btn btn-active btn-neutral w-1/8 text-white hover:bg-blue min-h-[35px] h-[40px] px-6"
                        style="background-color: #00428F;">Cadastrar</button>
                    <button class="btn btn-active btn-neutral w-1/6 text-white p-1 hover:bg-blue min-h-[35px] h-[40px]"
                        style="background-color: #00428F;">Salvar e cadastrar</button>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

interface manual {
    titulo: string
    perfil: string[],
    manual: string

}

const isEditing = ref(false)
const originalData = ref<manual | null>(null)

const optionSelected = ref({
    perfil: 'Médico',

})
const formData = reactive<manual>({
    titulo: '',
    perfil: [
        'Administrator',
        'Paciente',
        'Clínica',
        'Médico',
        'Recepcionista'
    ], manual: ''

})

function startEditing() {
    originalData.value = JSON.parse(JSON.stringify(formData))
    isEditing.value = true
}

function cancelEditing() {
    if (originalData.value) {
        Object.assign(formData, originalData.value)
    }
    isEditing.value = false
}

function saveChanges() {
    console.log('Saving changes:', formData)
    isEditing.value = false
}
</script>

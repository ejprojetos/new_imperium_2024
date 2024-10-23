<template>
    <LayoutDashboard>
        <div class="p-8">
            <div class="flex items-center justify-between mb-6 w-full max-w-[1000px] mx-auto">
                <div class="flex items-center">
                    <div class="w-24 h-24 mr-4 overflow-hidden rounded-full">
                        <img
                            src="../../../assets/placeholder.png"
                            alt="Profile"
                            class="object-cover w-full h-full" />
                    </div>
                    <h1 class="text-2xl font-bold">Administrador</h1>
                </div>
                <div class="p-4 bg-white rounded-lg shadow-md">
                    <h2 class="mb-2 text-2xl font-bold m-b">Pagamentos</h2>
                    <button class="w-full px-4 py-2 text-white bg-blue-600 rounded">
                        Acessar Asaas
                    </button>
                </div>
            </div>

            <div class="p-6 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto">
                <h2 class="mb-4 text-xl font-semibold">Dados Principais:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <template v-for="(value, key) in formData" :key="key">
                        <div
                            v-if="
                                [
                                    'clinicName',
                                    'responsibleName',
                                    'responsibleRG',
                                    'responsibleCPF',
                                    'cnpj'
                                ].includes(key)
                            ">
                            <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                            <input
                                v-if="isEditing"
                                v-model="formData[key]"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                            <p v-else>{{ value }}</p>
                        </div>
                    </template>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Endereço:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <template v-for="(value, key) in formData" :key="key">
                        <div
                            v-if="
                                [
                                    'country',
                                    'state',
                                    'city',
                                    'neighborhood',
                                    'zipCode',
                                    'street',
                                    'number'
                                ].includes(key)
                            ">
                            <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                            <input
                                v-if="isEditing"
                                v-model="formData[key]"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                            <p v-else>{{ value }}</p>
                        </div>
                    </template>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Contato:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <template v-for="(value, key) in formData" :key="key">
                        <div v-if="['email', 'phone'].includes(key)">
                            <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                            <input
                                v-if="isEditing"
                                v-model="formData[key]"
                                :type="key === 'email' ? 'email' : 'tel'"
                                class="w-full px-2 py-1 border rounded" />
                            <p v-else>{{ value }}</p>
                        </div>
                    </template>
                </div>

                <div class="flex justify-end mt-8">
                    <button
                        v-if="!isEditing"
                        @click="startEditing"
                        class="px-4 py-2 text-white bg-blue-600 rounded">
                        Editar
                    </button>
                    <template v-else>
                        <button
                            @click="cancelEditing"
                            class="px-4 py-2 mr-2 text-blue-600 bg-white border border-blue-600 rounded">
                            Cancelar
                        </button>
                        <button
                            @click="saveChanges"
                            class="px-4 py-2 text-white bg-blue-600 rounded">
                            Salvar
                        </button>
                    </template>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

const isEditing = ref(false)
const originalData = ref(null)

// #TODO: Escrever código que pega qual o tipo de usuário logado do state, para renderizar o nome do usuário e as permissoes corretas

const formData = reactive({
    clinicName: 'Dr. Alexandre',
    responsibleName: 'Alexandre de Melo Carneiro',
    responsibleRG: '000.000.000',
    responsibleCPF: '000.000.000-00',
    cnpj: '000-0',
    country: 'Brasil',
    state: 'RN',
    city: 'Parnamirim',
    neighborhood: 'Nova Parnamirim',
    zipCode: '59.999-999',
    street: 'Av. Maria Lacerda Montenegro',
    number: '000',
    email: 'exemplo99@gmail.com',
    phone: '(00) 0 0000-0000'
})

const labels = {
    clinicName: 'Nome da clínica',
    responsibleName: 'Nome do responsável',
    responsibleRG: 'RG do responsável',
    responsibleCPF: 'CPF do responsável',
    cnpj: 'CNPJ',
    country: 'País',
    state: 'Estado',
    city: 'Cidade',
    neighborhood: 'Bairro',
    zipCode: 'CEP',
    street: 'Logradouro',
    number: 'Número',
    email: 'Email',
    phone: 'Celular'
}

function startEditing() {
    originalData.value = JSON.parse(JSON.stringify(formData))
    isEditing.value = true
}

function cancelEditing() {
    Object.assign(formData, originalData.value)
    isEditing.value = false
}

function saveChanges() {
    console.log('Saving changes:', formData)
    isEditing.value = false
}
</script>

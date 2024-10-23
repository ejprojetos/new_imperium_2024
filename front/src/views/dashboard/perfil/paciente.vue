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
                    <h1 class="text-2xl font-bold">{{ formData.fullName }}</h1>
                </div>
                <div>
                    <button
                        @click="showPasswordModal = true"
                        class="px-4 py-2 text-white bg-blue-600 rounded">
                        Editar senha
                    </button>
                </div>
            </div>

            <div class="p-6 bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto">
                <h2 class="mb-4 text-xl font-semibold">Dados Pessoais:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <div v-for="(value, key) in personalInfo" :key="key">
                        <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                        <input
                            v-if="isEditing"
                            v-model="formData[key]"
                            :type="inputType(key)"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData[key] }}</p>
                    </div>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Endereço:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <div v-for="(value, key) in addressInfo" :key="key">
                        <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                        <input
                            v-if="isEditing"
                            v-model="formData[key]"
                            type="text"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData[key] }}</p>
                    </div>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Contato:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <div v-for="(value, key) in contactInfo" :key="key">
                        <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                        <div v-if="key === 'email'" class="flex items-center">
                            <input
                                v-if="isEditing"
                                v-model="formData[key]"
                                type="email"
                                class="w-full px-2 py-1 border rounded" />
                            <p v-else>{{ formData[key] }}</p>
                            <!--<button class="px-2 py-1 ml-2 text-sm text-white bg-blue-600 rounded">
                  Editar e-mail
                </button>-->
                        </div>
                        <input
                            v-else-if="isEditing"
                            v-model="formData[key]"
                            :type="inputType(key)"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData[key] }}</p>
                    </div>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">
                    Informações importantes para o médico:
                </h2>

                <div class="grid grid-cols-1 gap-4">
                    <div>
                        <label class="block mb-1 font-semibold">Alergias:</label>
                        <textarea
                            v-if="isEditing"
                            v-model="formData.allergies"
                            class="w-full px-2 py-1 border rounded"
                            rows="3"></textarea>
                        <p v-else>{{ formData.allergies }}</p>
                    </div>
                    <div>
                        <label class="block mb-1 font-semibold">Problemas recorrentes:</label>
                        <textarea
                            v-if="isEditing"
                            v-model="formData.recurringProblems"
                            class="w-full px-2 py-1 border rounded"
                            rows="3"></textarea>
                        <p v-else>{{ formData.recurringProblems }}</p>
                    </div>
                    <div>
                        <label class="block mb-1 font-semibold">Medicação:</label>
                        <div v-if="isEditing">
                            <textarea
                                v-if="isEditing"
                                v-model="formData.medication"
                                class="w-full px-2 py-1 border rounded"
                                rows="3"></textarea>
                        </div>
                        <p v-else>{{ formData.medications }}</p>
                    </div>
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
                            class="px-4 py-2 mr-2 text-gray-700 bg-gray-200 rounded">
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
            <ChangePasswordModal
                v-if="showPasswordModal"
                @close="showPasswordModal = false"
                @password-changed="handlePasswordChanged" />
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import ChangePasswordModal from '@/components/baseUi/ChangePasswordModal.vue'

const isEditing = ref(false)
const originalData = ref(null)

const formData = reactive({
    profileImage: '../../../assets/placeholder.png',
    fullName: 'Gabriele Rocha de Carvalho',
    birthDate: '10/10/1981',
    gender: 'Feminino',
    cpf: '999.999.999-99',
    country: 'Brasil',
    state: 'RN',
    city: 'Parnamirim',
    neighborhood: 'Nova Parnamirim',
    zipCode: '00000-000',
    street: 'Av. Ayrton Senna',
    number: '000',
    email: 'exemplo99@hotmail.com',
    phone: '(00) 00000-0000',
    allergies: '',
    recurringProblems: '',
    medications: ''
})

const personalInfo = {
    fullName: '',
    birthDate: '',
    gender: '',
    cpf: ''
}

const addressInfo = {
    country: '',
    state: '',
    city: '',
    neighborhood: '',
    zipCode: '',
    street: '',
    number: ''
}

const contactInfo = {
    email: '',
    phone: ''
}

const labels = {
    fullName: 'Nome completo',
    birthDate: 'Data de Nascimento',
    gender: 'Gênero',
    cpf: 'CPF',
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

function inputType(key: string): string {
    switch (key) {
        case 'birthDate':
            return 'date'
        case 'email':
            return 'email'
        case 'phone':
            return 'tel'
        default:
            return 'text'
    }
}

const showPasswordModal = ref(false)

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

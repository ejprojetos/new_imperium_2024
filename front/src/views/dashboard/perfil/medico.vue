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
                    <h1 class="text-2xl font-bold">{{ formData.personalInfo.fullName }}</h1>
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
                            v-model="formData.personalInfo[key]"
                            :type="inputType(key)"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData.personalInfo[key] }}</p>
                    </div>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Endereço:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <div v-for="(value, key) in addressInfo" :key="key">
                        <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                        <input
                            v-if="isEditing"
                            v-model="formData.addressInfo[key]"
                            type="text"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData.addressInfo[key] }}</p>
                    </div>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Contato:</h2>

                <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                    <div v-for="(value, key) in contactInfo" :key="key">
                        <label class="block mb-1 font-semibold">{{ labels[key] }}:</label>
                        <div v-if="key === 'email'" class="flex items-center">
                            <input
                                v-if="isEditing"
                                v-model="formData.contactInfo[key]"
                                type="email"
                                class="w-full px-2 py-1 border rounded" />
                            <p v-else>{{ formData.contactInfo[key] }}</p>
                            <!--<button class="px-2 py-1 ml-2 text-sm text-white bg-blue-600 rounded">
                  Editar e-mail
                </button>-->
                        </div>
                        <input
                            v-else-if="isEditing"
                            v-model="formData.contactInfo[key]"
                            :type="inputType(key)"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData.contactInfo[key] }}</p>
                    </div>
                </div>

                <h2 class="mt-6 mb-4 text-xl font-semibold">Dados Profissionais:</h2>

                <div class="grid grid-cols-1 gap-4">
                    <div>
                        <label class="block mb-1 font-semibold">Formação:</label>
                        <select
                            v-if="isEditing"
                            v-model="formData.education"
                            class="w-full px-2 py-1 border rounded">
                            <option value="Graduação e Pós-Graduação completo">
                                Graduação e Pós-Graduação completo
                            </option>
                            <!-- Add other options as needed -->
                        </select>
                        <p v-else>{{ formData.education }}</p>
                    </div>
                    <div>
                        <label class="block mb-1 font-semibold">Especialidade:</label>
                        <select
                            v-if="isEditing"
                            v-model="formData.specialty"
                            class="w-full px-2 py-1 border rounded">
                            <option value="Oftalmologia">Oftalmologia</option>
                            <!-- Add other options as needed -->
                        </select>
                        <p v-else>{{ formData.specialty }}</p>
                    </div>
                    <div>
                        <label class="block mb-1 font-semibold">Documentos comprobatórios:</label>
                        <button
                            v-if="isEditing"
                            @click="attachDocuments"
                            class="px-4 py-2 text-white bg-blue-600 rounded">
                            Anexar
                        </button>
                        <p v-else>{{ formData.documents }}</p>
                    </div>
                    <div>
                        <label class="block mb-1 font-semibold">CRM:</label>
                        <input
                            v-if="isEditing"
                            v-model="formData.crm"
                            type="text"
                            class="w-full px-2 py-1 border rounded" />
                        <p v-else>{{ formData.crm }}</p>
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

interface FormData {
  profileImage: string;
  personalInfo: {
    fullName: string;
    birthDate: string;
    gender: string;
    cpf: string;
  };
  addressInfo: {
    country: string;
    state: string;
    city: string;
    neighborhood: string;
    zipCode: string;
    street: string;
    number: string;
  };
  contactInfo: {
    email: string;
    phone: string;
  };
  education: string;
  specialty: string;
  documents: string;
  crm: string;
}

const isEditing = ref(false)
const originalData = ref(null)

const handlePasswordChanged = () => {
    console.log('Password changed:', '123')
}

const formData = reactive<FormData>({
  profileImage: '../../../assets/placeholder.png',
  personalInfo: {
    fullName: '',
    birthDate: '',
    gender: '',
    cpf: ''
  },
  addressInfo: {
    country: '',
    state: '',
    city: '',
    neighborhood: '',
    zipCode: '',
    street: '',
    number: ''
  },
  contactInfo: {
    email: '',
    phone: ''
  },
  education: '',
  specialty: '',
  documents: '',
  crm: ''
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
const attachDocuments = () => {
    console.log('Attaching documents')
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


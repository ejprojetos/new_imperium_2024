<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Cadastrar Clínica</h1>

            <div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
                <div class="flex items-center mb-6 gap-x-4">
                    <label class="block mb-2 text-2xl font-semibold">Imagem da clínica:</label>
                    <input
                        type="file"
                        accept="image/*"
                        @change="handleImageUpload"
                        class="hidden"
                        ref="fileInput" />
                    <button
                        @click="triggerFileInput"
                        class="px-2 py-2 text-white rounded bg-primary">
                        Escolher arquivo
                    </button>
                    <span v-if="selectedImage" class="ml-2">{{ selectedImage.name }}</span>
                </div>

                <form @submit.prevent="submitForm">
                    <h2 class="mb-4 text-xl font-semibold">Dados Principais:</h2>

                    <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                        <div>
                            <label class="block mb-1">Nome da clínica:</label>
                            <input
                                v-model="formData.clinicName"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Nome do responsável:</label>
                            <input
                                v-model="formData.responsibleName"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">RG do responsável:</label>
                            <input
                                v-model="formData.responsibleRG"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">CPF do responsável:</label>
                            <input
                                v-model="formData.responsibleCPF"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">CNPJ:</label>
                            <input
                                v-model="formData.cnpj"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                    </div>

                    <h2 class="mt-6 mb-4 text-xl font-semibold">Endereço:</h2>

                    <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                        <div>
                            <label class="block mb-1">País:</label>
                            <input
                                v-model="formData.country"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Estado:</label>
                            <input
                                v-model="formData.state"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Cidade:</label>
                            <input
                                v-model="formData.city"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Bairro:</label>
                            <input
                                v-model="formData.neighborhood"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">CEP:</label>
                            <input
                                v-model="formData.zipCode"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Logradouro:</label>
                            <input
                                v-model="formData.street"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Número:</label>
                            <input
                                v-model="formData.number"
                                type="text"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                    </div>

                    <h2 class="mt-6 mb-4 text-xl font-semibold">Contato:</h2>

                    <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
                        <div>
                            <label class="block mb-1">Email:</label>
                            <input
                                v-model="formData.email"
                                type="email"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                        <div>
                            <label class="block mb-1">Celular:</label>
                            <input
                                v-model="formData.phone"
                                type="tel"
                                class="w-full px-2 py-1 border rounded" />
                        </div>
                    </div>

                    <div class="flex justify-end mt-8 space-x-4">
                        <button
                            type="button"
                            @click="saveAndAddAnother"
                            class="px-4 py-2 text-white bg-blue-600 rounded">
                            Salvar e adicionar outra(o)
                        </button>
                        <button
                            type="button"
                            @click="saveAndContinueEditing"
                            class="px-4 py-2 text-white bg-blue-600 rounded">
                            Salvar e continuar editando
                        </button>
                        <button type="submit" class="px-4 py-2 text-white rounded bg-primary">
                            Salvar
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'

const fileInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)

// reactive pq formData é um objeto
const formData = reactive({
    clinicName: '',
    responsibleName: '',
    responsibleRG: '',
    responsibleCPF: '',
    cnpj: '',
    country: '',
    state: '',
    city: '',
    neighborhood: '',
    zipCode: '',
    street: '',
    number: '',
    email: '',
    phone: ''
})

const handleImageUpload = (event: Event) => {
    const target = event.target as HTMLInputElement
    if (target.files && target.files.length > 0) {
        selectedImage.value = target.files[0]
    }
}

const triggerFileInput = () => {
    fileInput.value?.click()
}

const submitForm = () => {
    console.log('Form submitted:', formData)
    console.log('Selected image:', selectedImage.value)
    toast.success('Salvo com sucesso!')
}

const saveAndAddAnother = () => {
    submitForm()
}

const saveAndContinueEditing = () => {
    submitForm()
}
</script>

<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Fluxo de trabalho</h1>

            <form @submit.prevent="submitForm">
                <!-- cards -->
                <div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
                    <p class="block mb-2 text-2xl font-semibold">Fluxo 1</p>
                    <div class="flex items-center mb-6 gap-x-4">
                        <label class="block mb-2 text-xl font-semibold">Imagem do ícone:</label>
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
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input type="text" class="w-full px-2 py-1 border rounded" />
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="phrase"
                            placeholder="Digite aqui a frase"
                            type="text"
                            class="w-full px-2 py-1 border rounded"
                            cols="60"
                            rows="6" />
                    </div>
                </div>

                <div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
                    <p class="block mb-2 text-2xl font-semibold">Fluxo 2</p>
                    <div class="flex items-center mb-6 gap-x-4">
                        <label class="block mb-2 text-xl font-semibold">Imagem do ícone:</label>
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
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input type="text" class="w-full px-2 py-1 border rounded" />
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="phrase"
                            placeholder="Digite aqui a frase"
                            type="text"
                            class="w-full px-2 py-1 border rounded"
                            cols="60"
                            rows="6" />
                    </div>
                </div>

                <div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
                    <p class="block mb-2 text-2xl font-semibold">Fluxo 3</p>
                    <div class="flex items-center mb-6 gap-x-4">
                        <label class="block mb-2 text-xl font-semibold">Imagem do ícone:</label>
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
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input type="text" class="w-full px-2 py-1 border rounded" />
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="phrase"
                            placeholder="Digite aqui a frase"
                            type="text"
                            class="w-full px-2 py-1 border rounded"
                            cols="60"
                            rows="6" />
                    </div>
                </div>

                <div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
                    <p class="block mb-2 text-2xl font-semibold">Fluxo 4</p>
                    <div class="flex items-center mb-6 gap-x-4">
                        <label class="block mb-2 text-xl font-semibold">Imagem do ícone:</label>
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
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input type="text" class="w-full px-2 py-1 border rounded" />
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="phrase"
                            placeholder="Digite aqui a frase"
                            type="text"
                            class="w-full px-2 py-1 border rounded"
                            cols="60"
                            rows="6" />
                    </div>
                </div>

                <div
                    class="flex justify-end mt-8 space-x-4 max-lg:flex-col max-lg:space-y-4 max-lg:space-x-0">
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
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'

const fileInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)

interface Fluxo {
    titulo: string
    descricao: string
    imagem: string
}

interface FormData {
    fluxo1: Fluxo
    fluxo2: Fluxo
    fluxo3: Fluxo
    fluxo4: Fluxo
}

const formData = reactive<FormData>({
    fluxo1: {
        titulo: '',
        descricao: '',
        imagem: ''
    },
    fluxo2: {
        titulo: '',
        descricao: '',
        imagem: ''
    },
    fluxo3: {
        titulo: '',
        descricao: '',
        imagem: ''
    },
    fluxo4: {
        titulo: '',
        descricao: '',
        imagem: ''
    }
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

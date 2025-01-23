<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Seção inicial</h1>

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
                    <h2 class="mb-4 text-xl font-semibold">Frase:</h2>

                    <div>
                        <textarea
                            v-model="phrase"
                            placeholder="Digite aqui a frase"
                            type="text"
                            class="w-full px-2 py-1 border rounded"
                            cols="60"
                            rows="10" />
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
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'
import { useInicialStore } from '@/stores/institucional/inicial.store'


const fileInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)
const inicialStore = useInicialStore()
const phrase = ref('')
const imagem = ref('')



onMounted(async () => {
    await inicialStore.fetchInicial()
    const firstItem = inicialStore.inicial[0]
    if(firstItem){
        phrase.value = firstItem.frase

        imagem.value = firstItem.imagem
    }
})

const handleImageUpload = (event: Event) => {
    const target = event.target as HTMLInputElement
    if (target.files && target.files.length > 0) {
        selectedImage.value = target.files[0]
        console.log('Imagem selecionada:', selectedImage.value)
    }
}

const triggerFileInput = () => {
    fileInput.value?.click()
}

const submitForm = async () => {
    if(!selectedImage.value || !phrase.value) {
        toast.error('Preencha todos os campos!')
        return
    }

    const formData = new FormData()
    formData.append('frase', phrase.value)
    if(selectedImage.value){
        formData.append('imagem', selectedImage.value)
    }

    
    try {
        const firstItem = inicialStore.inicial[0]
        if(firstItem){
            await inicialStore.updateInicial(firstItem.id, formData)
            toast.success('Atualizado com sucesso!')
            return
        }else{
            await inicialStore.creatInicial(formData)
            toast.success('Salvo com sucesso!')
        }
        //console.log('Dados enviados:', Array.from(formData.entries()))
        
        //const inicialData = formatPaginaInicialData();
        // await inicialStore.creatInicial(formData)
        // toast.success('Salvo com sucesso!')
    } catch (error) {
        toast.error('Erro ao salvar!')
        console.error(error)
    }
}

const saveAndAddAnother = () => {
    submitForm()
}

const saveAndContinueEditing = () => {
    submitForm()
}
</script>

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
                            @change="handleImageUpload($event, 'fluxo1')"
                            class="hidden"
                            ref="fileInput1" />
                        <button
                            @click.prevent="triggerFileInput('fileInput1')"
                            class="px-2 py-2 text-white rounded bg-primary">
                            Escolher arquivo
                        </button>
                        <span v-if="selectedImage1" class="ml-2">{{ selectedImage1 }}</span>
                    </div>
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input 
                        type="text" 
                        class="w-full px-2 py-1 border rounded"
                        v-model="formData.titulo1" />
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="formData.descricao1"
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
                            @change="handleImageUpload($event, 'fluxo2')"
                            class="hidden"
                            ref="fileInput2" />
                        <button
                            @click.prevent="triggerFileInput('fileInput2')"
                            class="px-2 py-2 text-white rounded bg-primary">
                            Escolher arquivo
                        </button>
                        <span v-if="selectedImage2" class="ml-2">{{ selectedImage2 }}</span>
                    </div>
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input type="text" class="w-full px-2 py-1 border rounded" 
                        v-model="formData.titulo2"/>
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="formData.descricao2"
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
                            @change="handleImageUpload($event, 'fluxo3')"
                            class="hidden"
                            ref="fileInput3" />
                        <button
                            @click.prevent="triggerFileInput('fileInput3')"
                            class="px-2 py-2 text-white rounded bg-primary">
                            Escolher arquivo
                        </button>
                        <span v-if="selectedImage3" class="ml-2">{{ selectedImage3 }}</span>
                    </div>
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input 
                        type="text" 
                        class="w-full px-2 py-1 border rounded"
                        v-model="formData.titulo3" 
                        />
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="formData.descricao3"
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
                            @change="handleImageUpload($event, 'fluxo4')"
                            class="hidden"
                            ref="fileInput4" />
                        <button
                            @click.prevent="triggerFileInput('fileInput4')"
                            class="px-2 py-2 text-white rounded bg-primary">
                            Escolher arquivo
                        </button>
                        <span v-if="selectedImage4" class="ml-2">{{ selectedImage4 }}</span>
                    </div>
                    <h2 class="mb-4 text-xl font-semibold">Titulo:</h2>
                    <div>
                        <input 
                        type="text" 
                        class="w-full px-2 py-1 border rounded" 
                        v-model="formData.titulo4"/>
                    </div>
                    <h2 class="my-4 text-xl font-semibold">Descrição:</h2>

                    <div>
                        <textarea
                            v-model="formData.descricao4"
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
import { ref, reactive, onMounted } from 'vue'
import type { Ref } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'
import type { FluxoDeTrabalho } from '@/types/institucional.types'
import { useFluxoStore } from '@/stores/institucional/fluxo.store'


const selectedImage1 = ref<File | null>(null)
const selectedImage2 = ref<File | null>(null)
const selectedImage3 = ref<File | null>(null)
const selectedImage4 = ref<File | null>(null)

const fluxoStore = useFluxoStore()

const fileInput1 = ref<HTMLInputElement | null>(null)
const fileInput2 = ref<HTMLInputElement | null>(null)
const fileInput3 = ref<HTMLInputElement | null>(null)
const fileInput4 = ref<HTMLInputElement | null>(null)


const formData = reactive<FluxoDeTrabalho>({
    id:'',
    uuid: '',
    titulo1: '',
    descricao1: '',
    imagem1: '',
    titulo2: '',
    descricao2: '',
    imagem2: '',
    titulo3: '',
    descricao3: '',
    imagem3: '',
    titulo4: '',
    descricao4: '',
    imagem4: '',
})

onMounted(async () =>{
    await fluxoStore.fetchFluxo()
    const firstItem = fluxoStore.fluxo[0]
    if(firstItem){
        formData.titulo1 = firstItem.titulo1
        formData.descricao1 = firstItem.descricao1
        formData.imagem1 = firstItem.imagem1
        formData.titulo2 = firstItem.titulo2
        formData.descricao2 = firstItem.descricao2
        formData.imagem2 = firstItem.imagem2
        formData.titulo3 = firstItem.titulo3
        formData.descricao3 = firstItem.descricao3
        formData.imagem3 = firstItem.imagem3
        formData.titulo4 = firstItem.titulo4
        formData.descricao4 = firstItem.descricao4
        formData.imagem4 = firstItem.imagem4
    }
})


const handleImageUpload = (event: Event, fluxo: string) => {
    const target = event.target as HTMLInputElement
    if (target.files && target.files.length > 0) {
        const file = target.files[0]
        // Armazenando o arquivo real, não apenas o nome
        if (fluxo === 'fluxo1') {
            selectedImage1.value = file
            formData.imagem1 = file.name
        } else if (fluxo === 'fluxo2') {
            selectedImage2.value = file
            formData.imagem2 = file.name
        } else if (fluxo === 'fluxo3') {
            selectedImage3.value = file
            formData.imagem3 = file.name
        } else if (fluxo === 'fluxo4') {
            selectedImage4.value = file
            formData.imagem4 = file.name
        }
    }
}


const triggerFileInput = (inputRef: string) => {
    const refMap: { [key: string]: Ref<HTMLInputElement | null> } = {
        fileInput1,
        fileInput2,
        fileInput3,
        fileInput4
    }
    const ref = refMap[inputRef]
    if(ref && ref.value) ref.value.click()
}


const submitForm = async () => {
    if(!formData.titulo1 || !formData.descricao1 || !formData.titulo2 || !formData.descricao2 || !formData.titulo3 || !formData.descricao3 || !formData.titulo4 || !formData.descricao4) {
        toast.error('Preencha todos os campos!')
        return
    }

    if (!formData.imagem1 || !formData.imagem2 || !formData.imagem3 || !formData.imagem4) {
        toast.error('Por favor, escolha todas as imagens!')
        return
    }

    const fd = new FormData()
    if(selectedImage1.value)fd.append('imagem1', selectedImage1.value)
    if(selectedImage2.value)fd.append('imagem2', selectedImage2.value)
    if(selectedImage3.value)fd.append('imagem3', selectedImage3.value)
    if(selectedImage4.value)fd.append('imagem4', selectedImage4.value)

    

    fd.append('titulo1', formData.titulo1)
    fd.append('descricao1', formData.descricao1)
    fd.append('titulo2', formData.titulo2)
    fd.append('descricao2', formData.descricao2)
    fd.append('titulo3', formData.titulo3)
    fd.append('descricao3', formData.descricao3)
    fd.append('titulo4', formData.titulo4)
    fd.append('descricao4', formData.descricao4)


    try{
        const firstItem = fluxoStore.fluxo[0]
        if(firstItem){
            await fluxoStore.updateFluxo(firstItem.id, fd)
        toast.success('Atualizado com sucesso!')
        return
    } else {
        await fluxoStore.creatFluxo(fd)
        toast.success('Salvo com sucesso!')
    }
    } catch (error) {
        console.log('Erro:', error)
    } 
    


    // console.log('Form submitted:', formData)
    // console.log('Selected image:', selectedImage.value)
    // toast.success('Salvo com sucesso!')
}

const saveAndAddAnother = () => {
    submitForm()
}

const saveAndContinueEditing = () => {
    submitForm()
}
</script>

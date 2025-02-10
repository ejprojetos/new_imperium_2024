<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="mb-6 text-4xl font-bold">Depoimentos</h1>

            <div class="p-6 mb-4 bg-white rounded-lg shadow-lg">
                <div class="flex items-center mb-6 gap-x-4">
                    <label class="block mb-2 text-2xl font-semibold">Imagem do autor:</label>
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
                    <h2 class="mb-4 text-xl font-semibold">Autor:</h2>
                    <input
                    v-model="autor"
                    placeholder="Digite aqui o autor"
                    class="w-full px-2 py-1 border rounded"
                    type="text"/>
                    
                    <h2 class="mt-5 mb-4 text-xl font-semibold">Depoimento:</h2>
                    <div>
                        <textarea
                            v-model="depoimento"
                            placeholder="Digite aqui a frase"
                            type="text"
                            class="w-full px-2 py-1 border rounded"
                            cols="60"
                            rows="8"
                            style="resize: none;" />
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
import { ref, onMounted} from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { useRoute } from 'vue-router'
import { useDepoimentoStore } from '@/stores/institucional/depoiment.store'
import { toast } from 'vue-sonner'


const fileInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)
const depoimentoStore = useDepoimentoStore()



const depoimento = ref('')
const autor = ref('')
const route = useRoute()
const id = route.params.id as string | undefined
const imagem = ref('')


onMounted( async () => {
    if(id){
        await depoimentoStore.fetchSingleDepoimento(id)
        autor.value = depoimentoStore.currentDepoimento?.nome || ''
        depoimento.value = depoimentoStore.currentDepoimento?.depoimento || ''
        imagem.value = depoimentoStore.currentDepoimento?.imagem || ''
    }else{  
        depoimentoStore.resetCurrentDepoimento()
    }
})

const handleImageUpload = () => {
    const target = fileInput.value
    selectedImage.value = target?.files ? target.files[0] : null
}

const triggerFileInput = () => {
    if(fileInput.value){
        fileInput.value.click()
    }
}

const submitForm = async () => {
    if(!autor.value || !depoimento.value ){
        toast.error('Preencha todos os campos')
        return
    }
    if(selectedImage.value){
        imagem.value = selectedImage.value.name
    }


    const data = new FormData()
    data.append('nome', autor.value)
    data.append('depoimento', depoimento.value)
    data.append('ativo', 'true')
    if(selectedImage.value){
        data.append('imagem', selectedImage.value)
    }


    try{
        if(id){
            await depoimentoStore.updateDepoimento(id, data)
            toast.success('Depoimento atualizado com sucesso')
        }else{
            await depoimentoStore.createDepoimento(data)
            toast.success('Depoimento criado com sucesso')
        }

        selectedImage.value = null
        autor.value = '';
        depoimento.value = '';
        
    } catch (error){
        toast.error('Erro ao salvar depoimento')
    }
}

 const saveAndAddAnother = () => {
     submitForm()
 }

const saveAndContinueEditing = () => {
    submitForm()
}
</script>
@/types/depoimento.types@/types/depoimento.type
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
                    type="text">
                    
                    <h2 class="mt-5 mb-4 text-xl font-semibold">Depoimento:</h2>
                    <div>
                        <textarea
                            v-model="phrase"
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
import { ref, onMounted } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { getDepoimentoById } from '@/services/depoimentos.service'
import { useRoute } from 'vue-router'
//import { submitDepoimento } from '@/services/depoimentos.service'
import { depoimentoService } from '@/services/depoimentos.service'
import { toast } from 'vue-sonner'
import { autoResetRef } from '@vueuse/core'

const fileInput = ref<HTMLInputElement | null>(null)
const selectedImage = ref<File | null>(null)
const phrase = ref('')
const autor = ref('')

const route = useRoute()
const id = route.params.id as string | undefined

//função para caso tenha depoimento cadastrado.
const carregarDepoimentoExistente = async () =>{
    if(id){
        try{
            //const depoimentoExistente =  await getDepoimentoById(id)
            const depoimentoExistente = await depoimentoService.getDepoimento(id)
            autor.value = depoimentoExistente.nome
            phrase.value = depoimentoExistente.depoimento
            //selectedImage.value = depoimentoExistente.imagem ? new File([depoimentoExistente.imagem], 'imagem.jpg'): null

            if(depoimentoExistente.imagem){
                const response = await fetch(depoimentoExistente.imagem);
                const blob = await response.blob();

                selectedImage.value = new File([blob], "imagem.jpg", {type: blob.type});
            }else{
                selectedImage.value = null;
            }
        } catch(error){
            toast.error('Erro ao carregar depoimento.')
            console.error(error)
        }
    }
}

onMounted(() =>{
    carregarDepoimentoExistente()
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

// const submitForm = () => {
//     console.log('Form submitted:', '123')
//     console.log('Selected image:', selectedImage.value)
//     toast.success('Salvo com sucesso!')
// }

const resetForm = () =>{
    autor.value = ''
    phrase.value = '';
    selectedImage.value = null;
}

const submitForm = async () =>{
    if(!phrase.value || !selectedImage.value){
        toast.error('Por favor, preencha todos os campos.')
        return;
    }

    // const formData = {
    //     depoimento: phrase.value,
    //     imagem: selectedImage.value
    // }
    
    const formData = new FormData();
    formData.append('nome', autor.value);
    formData.append('depoimento', phrase.value);
    if(selectedImage.value){
        formData.append('imagem', selectedImage.value)
    }

    try{
        // await submitDepoimento(formData);
        // toast.success('Depoimento salvo com sucesso!');
        // resetForm()
        if(id){
            await depoimentoService.updateDepoimento(id, formData);
            toast('Depoimento editado com sucesso!')
        }else{
            await depoimentoService.submitDepoimento(formData);
            toast.success
        }
        resetForm
    }catch(error){
        toast.error('Erro ao salvar depoimento');
        console.error(error);
    }
}




const saveAndAddAnother = () => {
    submitForm()
}

const saveAndContinueEditing = () => {
    submitForm()
}
</script>

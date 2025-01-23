<template>
    <div class="overflow-hidden bg-white shadow-lg rounded-3xl">
        <div class="flex items-center justify-between p-4 text-white bg-primary">
            <h2 class="text-xl font-semibold">Depoimentos</h2>
            <RouterLink to="/dashboard/institucional/cadastrar-depoimentos">
                <button
                    @click="navigateToAddDepoimento"
                    class="px-4 py-2 text-blue-600 transition-colors bg-white rounded-md hover:bg-blue-100">
                    Adicionar
                </button>
            </RouterLink>
        </div>
        <ul>
            <li
                v-for="depoimento in depoimentos"
                :key="depoimento.id"
                class="border-b last:border-b-0">
                <div class="flex items-center justify-between p-4 hover:bg-blue-200">
                    <span>{{ depoimento.nome }}</span>
                    <div class="max-lg:flex max-lg:flex-col max-lg:space-y-1">
                        <button
                            @click="editDepoimento(depoimento.id)"
                            class="px-3 py-1 mr-2 text-white transition-colors bg-blue-600 rounded-md hover:bg-blue-600 max-lg:w-full">
                            Editar
                        </button>
                        <button
                            @click="deleteDepoimento(depoimento.id)"
                            class="px-3 py-1 text-white transition-colors bg-red-500 rounded-md hover:bg-red-600">
                            Excluir
                        </button>
                    </div>
                </div>
            </li>
        </ul>

        <dialog ref="modalDelete" id="exclusao" class="modal">
            <div class="modal-box">
                <h3 class="text-xl font-bold text-center">Tem certeza que deseja excluir?</h3>
                <div class="flex justify-center gap-4 mt-4">
                    <button @click="closeModalDelete" class="text-black bg-gray-300 btn">
                        Cancelar
                    </button>
                    <button @click="confirmActionDelete" class="text-white btn bg-primary">
                        Confirmar
                    </button>
                </div>
            </div>
            <form method="dialog" class="modal-backdrop">
                <button>Fechar</button>
            </form>
        </dialog>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { Depoimento } from '@/types/institucional.types'
import { useDepoimentoStore } from '@/stores/institucional/depoiment.store'
import { reactify } from '@vueuse/core'
import { toast } from 'vue-sonner'

const router = useRouter()
const modalDelete = ref<HTMLDialogElement>()

const depoimentos = ref<Depoimento[]>([])
const depoimentoStore = useDepoimentoStore()




//depoimento que será excluido
const depoimentoParaExcluir = ref<Depoimento | null>(null)


onMounted(async () =>{
    try{
        await depoimentoStore.fetchDepoimentos()
        depoimentos.value = depoimentoStore.depoimentos
    } catch(error){
        console.error('Erro ao buscar depoimento', error)
    }
})


const closeModalDelete = () => {
    modalDelete.value?.close()
}

const showModalDelete = () => {
    modalDelete.value?.showModal()
}

const navigateToAddDepoimento = () => {
    router.push('/dashboard/institucional/cadastrar-depoimentos')
}

const editDepoimento = (id: string) => {
    depoimentoStore.fetchSingleDepoimento(id)
    router.push(`/dashboard/institucional/cadastrar-depoimentos/${id}`)
}

const deleteDepoimento = (id: string) => {
    const depoimento = depoimentos.value.find((d) => d.id === id)
    if(depoimento){
        depoimentoParaExcluir.value = depoimento
        showModalDelete()
    }
}
const confirmActionDelete =  async() => {
    if(depoimentoParaExcluir.value){
        try{
            await depoimentoStore.deleteDepoimento(depoimentoParaExcluir.value.id)
            depoimentos.value = depoimentos.value.filter((d) => d.id !== depoimentoParaExcluir.value?.id)
            closeModalDelete()
        }catch(error){
            toast.error('Erro ao excluir depoimento')
        }
    }
}

</script>

<style scoped>
ul {
    list-style: none;
    padding: 0;
}

ul li:nth-child(even) {
    background-color: #deecfa;
}
</style>

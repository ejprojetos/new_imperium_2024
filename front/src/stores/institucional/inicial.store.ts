import { inicialService } from "@/services/inicial.service"
import type { PaginaInicial } from "@/types/institucional.types"
import { defineStore } from "pinia"
import { ref } from "vue"


export const useInicialStore = defineStore('inicial', () => {
    const inicial = ref<PaginaInicial[]>([])
    const currentInicial = ref<PaginaInicial | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)



    const fetchInicial = async () => {
        try {
            loading.value = true

            inicial.value = await inicialService.getPaginaInicial()

        } catch (err){
            error.value = 'Erro ao buscar página inicial'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const creatInicial = async (inicialData: FormData) => {
        try {
            loading.value = true
            const newInicial = await inicialService.submitDepoimento(inicialData)
            inicial.value.push(newInicial)
            return newInicial

        } catch (err) {
            error.value = 'Erro ao criar página inicial'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }

        
    }

    const updateInicial = async (id: string, inicialData: FormData) => {
        try {
            if(!id) {
                throw new Error('ID não informado')
            }
            loading.value = true
            const updatedInicial = await inicialService.updateInicial(id, inicialData)
            const index = inicial.value.findIndex((c) => c.uuid === id)
            if (index !== -1) {
                inicial.value[index] = updatedInicial as PaginaInicial
            }
        } catch (err) {
            error.value = 'Erro ao atualizar página inicial'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }


    return{
        inicial,
        currentInicial,
        loading,
        error,
        fetchInicial,
        creatInicial,
        updateInicial
    }
})
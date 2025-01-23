import { fluxoService } from "@/services/fluxo.service";
import type { FluxoDeTrabalho } from "@/types/institucional.types";
import { defineStore } from "pinia";
import { ref } from "vue";


export const useFluxoStore = defineStore('fluxo', () => {
    const fluxo = ref<FluxoDeTrabalho[]>([])
    const currentFluxo = ref<FluxoDeTrabalho | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchFluxo = async () => {
        try{
            loading.value = true

            fluxo.value = await fluxoService.getFluxo()

        }catch(err){
            error.value = 'Erro ao buscar fluxo de trabalho'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const creatFluxo = async (inicialData: FormData) => {
        try{
            loading.value = true
            const newFluxo = await fluxoService.submitFluxo(inicialData)
            fluxo.value.push(newFluxo)
            return newFluxo
        }catch(err){
            error.value = 'Erro ao criar fluxo de trabalho'
            console.error(err)
            throw err
        }finally{
            loading.value = false
        }
    }

    const updateFluxo = async (id: string, fluxoData: FormData) => {
        try{
            if(!id){
                throw new Error('Id não informado')
            }
            loading.value = true
            const updateFluxo = await fluxoService.updateFluxo(id, fluxoData)
            const index = fluxo.value.findIndex((c) => c.uuid === id)
            if(index !== -1){
                fluxo.value[index] = updateFluxo as FluxoDeTrabalho
            }
        }catch(err){
            error.value = 'Erro ao atualizar fluxo de trabalho'
            console.error(err)
            throw err
        }finally{
            loading.value = false
        }
    }

    return{
        fluxo,
        currentFluxo,
        loading,
        error,
        fetchFluxo,
        creatFluxo,
        updateFluxo
    }
})
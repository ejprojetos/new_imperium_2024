import { defineStore } from "pinia";
import { ref } from "vue";
import type { Depoimento } from "@/types/depoimentos.types";
import { depoimentoService } from "@/services/depoimentos.service";m

export const useDepoimentStore = defineStore('depoiment', () => {
    const depoiments = ref< Depoimento[]>([])
    const currentDepoiment = ref<Depoimento | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchDepoiments =  async () =>{
        try{
            loading.value = true
            depoiments.value = await depoimentoService.getAllDepoiments()
        }catch(err){
            error.value = 'Erro ao buscar depoimentos'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const createDepoiment =  async(depoimentData: Partial<Depoimento>) => {
        try{
            loading.value = true
            const newDepoiment = await depoimentoService.createDepoiment(depoimentData)
            depoiments.value.push(newDepoiment)
            return newDepoiment
        } catch(err){
            error.value = 'Erro ao criar depoimento'
            console.error(err)
            throw err
        } finally{
            loading.value = false
        }
    }




    return{
        depoiments,
        currentDepoiment,
        loading,
        error,
        fetchDepoiments,
        createDepoiment
    }
})
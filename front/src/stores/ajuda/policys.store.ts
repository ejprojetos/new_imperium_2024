import { ajudaService, policiesService } from "@/services/ajuda.service";
import { defineStore } from "pinia";
import { ref } from "vue";
import type { Policies } from "@/types/ajuda.types";


export const usePolicyStore = defineStore('policy', () => {
    const policies = ref<Policies[]>([])
    const currentPolicy = ref<Policies | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchPolicies = async() =>{
        try{
            loading.value = true
            if(!policies.value.length){
                policies.value = await policiesService.getAllPolicies()
            }
        } catch(err){
            error.value = 'Erro ao buscar politicas'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const fetchSinglePolicy = async(id: number) => {
        try{
            loading.value = true
            currentPolicy.value = await policiesService.getPolicy(id)
        }catch(err){
            error.value = 'Erro ao buscar politica'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const createPolicy = async(policyData: Partial<Policies>) =>{
        try{
            loading.value = true
            const newPolicy = await policiesService.createPolicy(policyData)
            policies.value.push(newPolicy)
            return newPolicy
        }catch(err){
            error.value = 'Erro ao criar faq'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const updatePolicy = async (id: number, policyData: Partial<Policies>) =>{
        try{
            loading.value = true
            const updatePolicy = await policiesService.updatePolicy(id, policyData)

            if(!updatePolicy){
                throw new Error('Erro ao atualizar política'
                )
            }

            const index = policies.value.findIndex(policy => policy.id === id)
            policies.value[index] = updatePolicy

            return updatePolicy
        }catch(err){
            error.value = 'Erro ao atualizar política'
            console.error(err)
        } finally{
            loading.value = false
        }  
    }   

    const deletPolicy = async (id: number) =>{
        try{
            loading.value = true
            await policiesService.deletPolicy(id)
            policies.value = policies.value.filter(policy => policy.id !== id)
        }catch(err){
            error.value = 'Erro ao deletar política'
            console.error(err)
        }
        finally{
            loading.value = false
        }
    }


    return{
        policies,
        currentPolicy,
        loading,
        error,
        fetchPolicies,
        fetchSinglePolicy,
        createPolicy,
        updatePolicy,
        deletPolicy
    }
})
import { featureService } from "@/services/features.service";
import type { Feature } from "@/types/institucional.types";
import { defineStore } from "pinia";
import { ref } from "vue";




export const useFeatureStore = defineStore('feature', () => {
    const features = ref<Feature[]>([])
    const currentFeature = ref<Feature | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchFeature = async () => {
        try{
            loading.value = true

            features.value = await featureService.getFeatures()

        }catch(err){
            error.value = 'Erro ao buscar feature'
            console.error(err)
        }finally{
            loading.value = false
        }
    }

    const creatFeature = async (inicialData: FormData) => {
        try{
            loading.value = true
            const newFeature = await featureService.submitFeature(inicialData)
            features.value.push(newFeature)
            return newFeature
        }catch(err){
            error.value = 'Erro ao criar feature'
            console.error(err)
            throw err
        }finally{
            loading.value = false
        }
    }

    const updateFeature = async (id: string, featureData: FormData) => {
        try{
            if(!id){
                throw new Error('Id não informado')
            }
            loading.value = true
            const updateFeature = await featureService.updateFeature(id, featureData)
            const index = features.value.findIndex((c) => c.uuid === id)
            if(index !== -1){
                features.value[index] = updateFeature as Feature
            }
        }catch(err){
            error.value = 'Erro ao atualizar feature'
            console.error(err)
            throw err
        }finally{
            loading.value = false
        }
    }

    return{
        features,
        currentFeature,
        loading,
        error,
        fetchFeature,
        creatFeature,
        updateFeature
    }
})
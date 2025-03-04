import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Clinic } from '@/types/clinic.types'
import { clinicService } from '@/services/clinic.service'

export const useClinicStore = defineStore('clinic', () => {
    const clinics = ref<Clinic[]>([])
    const currentClinic = ref<Clinic | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchClinics = async () => {
        try {
            loading.value = true
            if (!clinics.value.length) {
                clinics.value = await clinicService.getAllClinics()
            }
        } catch (err) {
            error.value = 'Erro ao buscar clínicas'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    const fetchSingleClinic = async (id: string) => {
        try {
            loading.value = true
            currentClinic.value = await clinicService.getClinic(id)
        } catch (err) {
            error.value = 'Erro ao buscar clínica'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    
    const createClinic = async (clinicData: Partial<Clinic>) => {
        try {
            loading.value = true
            const newClinic = await clinicService.createClinic(clinicData)
            clinics.value.push(newClinic)
            return newClinic
        } catch (err) {
            error.value = 'Erro ao criar clínica'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    const updateClinic = async (id: number, clinicData: Partial<Clinic>) => {
        try {
            loading.value = true

            const updatedClinic = await clinicService.updateClinic(id, clinicData)

            if(!updatedClinic) {
                throw new Error('Erro ao atualizar clínica')
            }

            console.log('Lista de clinicas antes da atualização:', clinics.value)
            const index = clinics.value.findIndex((c) => c.id === id) // encontra o index da clínica a ser atualizada
            if (index !== -1) {
                clinics.value[index] = updatedClinic // atualiza a clínica no array
            }else{
                console.warn('Clínica não encontrada no array de clínicas')
            }
            
            return updatedClinic
        } catch (err) {
            error.value = 'Erro ao atualizar clínica'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    const deleteClinic = async (id: string) => {
        try {
            loading.value = true
            await clinicService.deleteClinic(id)
            clinics.value = clinics.value.filter((c) => c.uuid !== id) // filtra a clínica excluida localmente
        } catch (err) {
            error.value = 'Erro ao excluir clínica'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    return {
        clinics,
        currentClinic,
        loading,
        error,
        fetchClinics,
        createClinic,
        updateClinic,
        deleteClinic,
        fetchSingleClinic
    }
})

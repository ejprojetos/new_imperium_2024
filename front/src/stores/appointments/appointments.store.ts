import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Appointment, AppointmentResponse } from '@/types/appointments.types'
import { appointmentService } from '@/services/appointments.service'

export const useAppointmentStore = defineStore('appointment', () => {
    const appointments = ref<AppointmentResponse[]>([])
    const currentAppointment = ref<AppointmentResponse | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchAppointments = async () => {
        try {
            loading.value = true
            if (!appointments.value.length) {
                appointments.value = await appointmentService.getAll()
            }
        } catch (err) {
            error.value = 'Erro ao buscar consultas'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    const fetchSingleAppointment = async (uuid: string) => {
        try {
            loading.value = true
            currentAppointment.value = await appointmentService.getOne(uuid)
        } catch (err) {
            error.value = 'Erro ao buscar consulta'
            console.error(err)
        } finally {
            loading.value = false
        }
    }

    const createAppointment = async (data: Partial<Appointment>) => {
        try {
            loading.value = true
            const newAppointment = await appointmentService.create(data)
            appointments.value.push(newAppointment)
            return newAppointment
        } catch (err) {
            error.value = 'Erro ao criar consulta'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    const updateAppointment = async (uuid: string, data: Partial<Appointment>) => {
        try {
            loading.value = true
            const updatedAppointment = await appointmentService.update(uuid, data)
            const index = appointments.value.findIndex((a) => a.uuid === uuid)
            if (index !== -1) {
                appointments.value[index] = updatedAppointment
            }
            return updatedAppointment
        } catch (err) {
            error.value = 'Erro ao atualizar consulta'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    const deleteAppointment = async (uuid: string) => {
        try {
            loading.value = true
            await appointmentService.delete(uuid)
            appointments.value = appointments.value.filter((a) => a.uuid !== uuid)
        } catch (err) {
            error.value = 'Erro ao excluir consulta'
            console.error(err)
            throw err
        } finally {
            loading.value = false
        }
    }

    return {
        appointments,
        currentAppointment,
        loading,
        error,
        fetchAppointments,
        fetchSingleAppointment,
        createAppointment,
        updateAppointment,
        deleteAppointment
    }
})

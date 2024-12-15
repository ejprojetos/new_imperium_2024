import { ref, computed } from 'vue'

interface Clinic {
    id: number
    name: string
    address?: string
    isActive?: boolean
}

const clinics = ref<Clinic[]>([
    { id: 1, name: 'Clínica Dr. Alexandre', isActive: true },
    { id: 2, name: 'Clínica Maxado de Assis', isActive: true },
    { id: 3, name: 'Clínica Odontológica Merci', isActive: true },
    { id: 4, name: 'Clínica LolOdonto', isActive: true },
    { id: 5, name: 'Clínica OdontoMed', isActive: true },
    { id: 6, name: 'Clínica Sorriso', isActive: true }
])

export function useClinicStore() {
    const activeClinics = computed(() => clinics.value.filter(clinic => clinic.isActive))

    const addClinic = (clinic: Omit<Clinic, 'id' | 'isActive'>) => {
        const newId = Math.max(...clinics.value.map(c => c.id)) + 1
        clinics.value.push({
            ...clinic,
            id: newId,
            isActive: true
        })
    }

    const updateClinic = (id: number, data: Partial<Clinic>) => {
        const index = clinics.value.findIndex(c => c.id === id)
        if (index !== -1) {
            clinics.value[index] = {
                ...clinics.value[index],
                ...data
            }
        }
    }

    const deactivateClinic = (id: number) => {
        updateClinic(id, { isActive: false })
    }

    const getClinicById = (id: number) => {
        return clinics.value.find(c => c.id === id)
    }

    return {
        clinics,
        activeClinics,
        addClinic,
        updateClinic,
        deactivateClinic,
        getClinicById
    }
} 
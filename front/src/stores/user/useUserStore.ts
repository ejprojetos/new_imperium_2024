import { defineStore } from 'pinia'
import { ref } from 'vue'

type USER_ROLE = 'ADMIN' | 'DOCTOR' | 'PATIENT' | 'RECEPTIONIST'

type User = {
    role: USER_ROLE
    name: string
    id: number
}

export const useUserStore = defineStore(
    'user',
    () => {
        const idRef = ref<number | null>(null)
        const roleRef = ref<USER_ROLE>('PATIENT')

        const setUser = ({ role, id }: User) => {
            idRef.value = id
            roleRef.value = role
        }

        return {
            id: idRef,
            role: roleRef,
            setUser
        }
    },
    {
        persist: true
    }
)

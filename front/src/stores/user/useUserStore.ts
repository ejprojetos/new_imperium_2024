import { defineStore } from 'pinia'
import { ref } from 'vue'

type UserRole = 'ADMIN' | 'DOCTOR' | 'PATIENT' | 'RECEPTIONIST'


export const useUserStore = defineStore(
    'user',
    () => {
        const role = ref<UserRole>('PATIENT')
        const name = ref('Admin')

        const setUser = (newRole: UserRole, newName: string) => {
            role.value = newRole
            console.log('role no store', newRole)
            name.value = newName
        }
    
        return {
            role,
            name,
            setUser
        }
    },
    {
        persist: true
    }
)

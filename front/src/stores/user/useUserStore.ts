import { defineStore } from 'pinia'
import { ref } from 'vue'

type UserRole = 'admin' | 'superadmin' | 'medico' | 'recepcionista' | 'paciente'

export const useUserStore = defineStore('user', () => {
    const role = ref<UserRole>('admin')
    const name = ref('Admin')

    const setRole = (newRole: UserRole) => {
        role.value = newRole
        name.value = setName(newRole)
    }

    const setName = (role: string) => {
        let nome: string
        switch (role) {
            case 'admin':
                nome = 'Admin'
                break
            case 'superadmin':
                nome = 'Superadmin'
                break
            case 'medico':
                nome = 'Médico'
                break
            case 'recepcionista':
                nome = 'Recepcionista'
                break
            case 'paciente':
                nome = 'Paciente'
                break
            default:
                nome = 'Usuário'
        }
        return nome
    }

    return {
        role,
        name,
        setRole
    }
})

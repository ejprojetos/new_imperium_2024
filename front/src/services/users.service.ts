import { fetcher } from './fetcher.service'
import type { User } from '@/types/users.types'

// adiciona interface para validação de erros
interface ValidationErrors {
    [key: string]: string[]
}

export const userService = {
    getDoctors: () => fetcher<User[]>('/users/users_doctors'),
    getPatients: () => fetcher<User[]>('/users/users_pacientes'),
    getUserById: (id: string) => fetcher<User>(`/users/${id}`),
    createDoctor: async (data: any) => {
        // usa a url base da api
        const baseURL = import.meta.env.VITE_API_URL
        const response = await fetch(`${baseURL}/users/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...(localStorage.getItem('token') && {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                })
            },
            body: JSON.stringify(data)
        })

        // verifica se a resposta não foi bem sucedida
        if (!response.ok) {
            const errorData = await response.json()
            throw {
                status: response.status,
                errors: errorData as ValidationErrors
            }
        }

        return response.json()
    }
}

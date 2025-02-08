import { fetcher } from './fetcher.service'
import type { User } from '@/types/users.types'

// adiciona interface para validação de erros
interface ValidationErrors {
    [key: string]: string[]
}

export const userService = {
    getDoctors: () => fetcher<User[]>('/users/users_doctors'),
    getPatients: () => fetcher<User[]>('/users/users_pacientes'),
    getReceptionists: () => fetcher<User[]>('/users/users_recepcionistas'),
    getUserById: (id: string) => fetcher<User>(`/users/${id}`),
    createDoctor: async (data: any) => {
        // usa a url base da api
        const baseURL = import.meta.env.VITE_API_URL
        const token = localStorage.getItem('access_token')
        // console log do token
        if (token) {
            console.log('Token:', token)
        } else {
            console.error('No token found in localStorage')
        }
        const response = await fetch(`${baseURL}/users/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...(localStorage.getItem('access_token') && {
                    Authorization: `Bearer ${localStorage.getItem('access_token')}`
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
    },
    createReceptionist: async (data: any) => {
		const baseURL = import.meta.env.VITE_API_URL
		const token = localStorage.getItem('access_token')
        // console log do token
        if (token) {
            console.log('Token:', token)
        } else {
            console.error('No token found in localStorage')
        }
        const response = await fetch(`${baseURL}/users/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...(localStorage.getItem('access_token') && {
                    Authorization: `Bearer ${localStorage.getItem('access_token')}`
                })
            },
			body: JSON.stringify({
				...data,
				roles: [
					{ name: 'RECEPTIONIST' }
				]
			})
        })

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

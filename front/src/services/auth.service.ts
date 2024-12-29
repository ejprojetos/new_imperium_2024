import { fetcher } from './fetcher.service'
import { useRouter } from 'vue-router'

export interface LoginData {
    email: string
    password: string
}

export interface LoginResponse {
    access: string
    refresh: string
    detail: string | null
    role?: string
}

export const authService = {
    login: async (data: LoginData) => {
        try {
            const response = await fetcher<LoginResponse>('/auth/token/', {
                method: 'POST',
                body: JSON.stringify(data)
            })

            console.log('Login response', response)
            if (response.detail) {
                throw new Error(response.detail)
            }

            if (response.access) {
                localStorage.setItem('access_token', response.access)
                localStorage.setItem('refresh_token', response.refresh)
                localStorage.setItem('user_role', 'admin') // TODO: remover quando a api voltar o role corretamente
                if (response.role) {
                    localStorage.setItem('user_role', response.role)
                }
            }

            return response
        } catch (error) {
            console.error(error)
            throw error
        }
    },

    refreshToken: (data: LoginData) =>
        fetcher<LoginResponse>('/auth/refresh/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    logout: () => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('user_role')

        const router = useRouter()
        router.push('/auth/login')

        return fetcher('/auth/logout/', {
            method: 'POST'
        })
    }
}

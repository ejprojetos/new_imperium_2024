import { fetcher } from './fetcher.service'
import { useRouter } from 'vue-router'
import type { LoginData, LoginResponse } from '@/types/auth.types'

export const authService = {
    login: async (data: LoginData) => {
        try {
            const response = await fetcher<LoginResponse>('/auth/token/', {
                method: 'POST',
                body: JSON.stringify(data)
            })

            if (!response) {
                throw new Error('Login response is null')
            }

            console.log('Login response', response)
            if (response.detail) {
                throw new Error(response.detail)
            }

            if (response.access) {
                localStorage.setItem('access_token', response.access)
                localStorage.setItem('refresh_token', response.refresh)
                localStorage.setItem('user_role', response.user_role[0])
            }

            return response as LoginResponse
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

    // servico para solicitar recuperacao de senha
    requestPasswordReset: async (email: string) => {
        try {
            const response = await fetcher('/password-reset/', {
                method: 'POST',
                body: JSON.stringify({ email })
            })
            return response
        } catch (error) {
            console.error('erro ao solicitar recuperacao de senha:', error)
            throw error
        }
    },

    // servico para confirmar a nova senha
    confirmPasswordReset: async (token: string, newPassword: string) => {
        try {
            const response = await fetcher('/password-reset-confirm/', {
                method: 'POST',
                body: JSON.stringify({
                    token,
                    new_password: newPassword
                })
            })
            return response
        } catch (error) {
            console.error('erro ao confirmar nova senha:', error)
            throw error
        }
    },

    logout: () => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.removeItem('user_role')

        //const router = useRouter()
        //router.push('/auth/login')

        //return fetcher('/auth/logout/', {
        //    method: 'POST'
        //})
    }
}

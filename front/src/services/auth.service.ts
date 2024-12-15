import { fetcher } from './fetcher.service'

export interface LoginData {
    email: string
    password: string
}

// TODO: Verificar se vai ser isso mesmo
export interface LoginResponse {
    access: string
    refresh: string
    user: {
        id: number
        email: string
        role: string
    }
}

export const authService = {
    login: (data: LoginData) =>
        fetcher<LoginResponse>('/auth/login/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    logout: () =>
        fetcher('/auth/logout/', {
            method: 'POST'
        })
}

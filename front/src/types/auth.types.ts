export interface LoginData {
    email: string
    password: string
}

export interface LoginResponse {
    access: string
    refresh: string
    detail: string | null
    user_role: string
    name: string
}

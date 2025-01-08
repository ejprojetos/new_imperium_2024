const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://172.105.155.145/api' // TODO: Mover para .env e colocar a url do servidor de produção

export async function fetcher<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const token = localStorage.getItem('access_token')

    // const headers: HeadersInit = {
    //     'Content-Type': 'application/json',
    //     ...(token && { Authorization: `Bearer ${token}` }),
    //     ...options.headers
    // }

    //mudança para receber tanto json como formData.
    const headers: HeadersInit = {
        ...(token && {Authorization: `Bearer ${token}`}),
        ...(!options.body || !(options.body instanceof FormData) ? {'Content-Type': 'application/json'} : {}),
        ...options.headers,

    }

    const response = await fetch(`${BASE_URL}${endpoint}`, {
        ...options,
        headers
    })
    if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || response.statusText)
    }

    return response.json()
}

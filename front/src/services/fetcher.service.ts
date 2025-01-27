const BASE_URL = import.meta.env.VITE_API_URL

export async function fetcher<T>(endpoint: string, options: RequestInit = {}): Promise<T | null> {
    const token = localStorage.getItem('access_token')

    //mudança para receber tanto json como formData.
    const headers: HeadersInit = {
        ...(token && { Authorization: `Bearer ${token}` }),
        ...(!options.body || !(options.body instanceof FormData)
            ? { 'Content-Type': 'application/json' }
            : {}),
        ...options.headers
    }

    try {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
            ...options,
            headers
        })

        if (!response.ok) {
            let errorData = null
            try {
                errorData = await response.json()
            } catch (err) {
                errorData = { detail: response.statusText }
            }
            throw new Error(errorData.detail || response.statusText)
        }

        if (response.status === 204) {
            return null
        }

        return await response.json()
    } catch {
        console.error('Erro ao fazer requisição')
        return null
    }
}

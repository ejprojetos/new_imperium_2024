const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://172.105.155.145/api'

export async function fetcher<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const token = localStorage.getItem('access_token')

    const headers: HeadersInit = {
        'Content-Type': 'application/json',
        ...(token && { Authorization: `Bearer ${token}` }),
        ...options.headers
    }

    const response = await fetch(`${BASE_URL}${endpoint}`, {
        ...options,
        headers
    })

    if (!response.ok) {
        throw new Error('API Error')
    }

    return response.json()
}

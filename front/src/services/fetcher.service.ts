const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://172.105.155.145/api' // TODO: Mover para .env e colocar a url do servidor de produção

export async function fetcher<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    // const token = localStorage.getItem('access_token')
    const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0OTk5MDQwLCJpYXQiOjE3MzQ5OTU0NDAsImp0aSI6ImNkYTNhNjkzMmVmNzQ3ZDBhOWVhNDg2NTc1NjY0OTAxIiwidXNlcl9pZCI6Nn0.MRPAHArJOl0Fw2Q_8Y_T3PGIUnqJnD_rtCh5fEnk31s'

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
        const errorData = await response.json()
        throw new Error(errorData.detail || response.statusText)
    }

    return response.json()
}

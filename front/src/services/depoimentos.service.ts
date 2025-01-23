import type { Depoimento } from '@/types/depoimentos.types'
import { fetcher } from './fetcher.service'

export const depoimentoService = {
    //buscar todos os depoimentos
    getAllDepoimentos: () => fetcher<Depoimento[]>('/institucional/depoimento'),

    //buscar pelo id
    getDepoimento: (id: string) => fetcher<Depoimento>(`/institucional/depoimento/${id}`),

    //criar novo depoimento
    submitDepoimento: (data: FormData) =>
        fetcher<Depoimento>('/institucional/depoimento', {
            method: 'POST',
            body: data
        }),

    //editar depoimento
    updateDepoimento: (id: string, data: FormData) =>
        fetcher(`/institucional/depoimento/${id}/`, {
            method: 'PUT',
            body: data
        })
}

export async function getDepoimentos(): Promise<Depoimento[]> {
    const url = 'http://161.35.63.22/api/institucional/depoimento/'

    try {
        const response = await fetch(url)

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`)
        }

        const data: Depoimento[] = await response.json()
        return data
    } catch (error) {
        console.log('Erro ao buscar depoimentos:', error)
        throw error
    }
}

export async function getDepoimentoById(id: string): Promise<Depoimento> {
    const url = `http://161.35.63.22/api/institucional/depoimento/${id}`

    try {
        const response = await fetch(url)
        if (!response.ok) {
            throw new Error(`Http error! Status: ${response.status}`)
        }
        const data: Depoimento = await response.json()
        return data
    } catch (error) {
        console.error('Erro ao buscar depoiemento:', error)
        throw error
    }
}

export async function submitDepoimento(formData: Depoimento): Promise<void> {
    const url = 'http://161.35.63.22/api/institucional/depoimento/'

    const token = localStorage.getItem('access_token')

    if (!token) {
        console.error('Token de acesso não encontrado. O usuário pode não estar logado.')
        return
    }

    const form = new FormData()
    form.append('nome', 'Precisa de espaço para colocar o autor')
    form.append('depoimento', formData.depoimento)
    if (formData.imagem) {
        form.append('imagem', formData.imagem)
    }

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                Authorization: `Bearer ${token}`
            },
            body: form
        })

        if (!response.ok) {
            throw new Error(`Erro ao enviar dados! Status: ${response.status}`)
        }
        console.log('Dados enviados com sucesso!')
    } catch (error) {
        console.error('Erro ao enviar formulário', error)
        throw error
    }
}

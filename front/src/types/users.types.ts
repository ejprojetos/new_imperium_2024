import type { Address } from './clinic.types'

export interface User {
    id: number
    first_name: string
    last_name: string
    email: string
    cpf: string
    date_birth: string
    address: Address
    clinics: number[]
    gender: string
    formacao: string
    crm: string
    attach_document: string
    password?: string
}

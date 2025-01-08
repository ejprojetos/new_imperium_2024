export interface Address {
    country: string
    state: string
    city: string
    neighborhood: string
    zipCode: string
    street: string
    number: string
}

export interface Clinic {
    uuid: string
    name: string
    cnpj: string
    //Acrescentado após modificação no endpoint
    image:string
    telefone_responsavel: string
    email_responsavel:string
    cpf_responsavel: string
    nome_responsavel: string
    rg_responsavel: string

    //is_active: boolean
    address: Address
    //admin_clinic: string // user ID
}

export interface Room {
    uuid: string
    clinic: string // clinic ID
    number: string
    description: string
}

export interface MedicalRecord {
    uuid: string
    patient: string
    doctor: string
    appointment: string
    allergies: string
    issues: string
    medication: string
    anamnesis: string
    new_medication: string
    exams: string
}

export interface Appointment {
    uuid: string
    patient: string
    doctor: string
    clinic: string
    appointment_date: string
    reason: string
    status: 'scheduled' | 'canceled' | 'completed'
}

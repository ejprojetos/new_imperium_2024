type AppointmentStatus = 'scheduled' | 'canceled' | 'completed'

export interface Appointment {
    uuid?: string
    patient: number
    doctor: number
    clinic: number
    appointment_date: string
    reason: string
    status?: AppointmentStatus
    room: number
}

export interface AppointmentResponse extends Appointment {
    uuid: string
    status: AppointmentStatus
    patient_name: string
    doctor_name: string
    clinic_name: string
}

export interface AppointmentDelete {
    uuid: string
}

import { fetcher } from './fetcher.service'
import type {
    Appointment,
    AppointmentResponse,
    AppointmentDelete
} from '@/types/appointments.types'

export const appointmentService = {
    getAll: () => fetcher<AppointmentResponse[]>('/appointments/'),

    getOne: (uuid: string) => fetcher<AppointmentResponse>(`/appointments/${uuid}/`),

    create: (data: Partial<Appointment>) =>
        fetcher<AppointmentResponse>('/appointments/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    update: (uuid: string, data: Partial<Appointment>) =>
        fetcher<AppointmentResponse>(`/appointments/${uuid}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    delete: (uuid: string) =>
        fetcher<AppointmentDelete>(`/appointments/${uuid}/`, {
            method: 'DELETE'
        })
}

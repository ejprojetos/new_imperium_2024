import { fetcher } from './fetcher.service'
import type { Clinic, Room, MedicalRecord, Appointment } from '@/types/clinic.types'

export const clinicService = {
    // Endopoins definidos no app Clinicas
    getAllClinics: () => fetcher<Clinic[]>('/clinics/'),

    getClinic: (id: string) => fetcher<Clinic>(`/clinics/${id}/`),

    createClinic: (data: Partial<Clinic>) =>
        fetcher<Clinic>('/clinics/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    updateClinic: (id: string, data: Partial<Clinic>) =>
        fetcher<Clinic>(`/clinics/${id}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    deleteClinic: (id: string) =>
        fetcher(`/clinics/${id}/`, {
            method: 'DELETE'
        }),

    // Rooms
    getRooms: (clinicId: string) => fetcher<Room[]>(`/clinics/${clinicId}/rooms/`),

    getRoom: (clinicId: string, uuid: string) =>
        fetcher<Room>(`/clinics/${clinicId}/rooms/${uuid}/`),

    createRoom: (clinicId: string, data: Partial<Room>) =>
        fetcher<Room>(`/clinics/${clinicId}/rooms/`, {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    updateRoom: (clinicId: string, uuid: string, data: Partial<Room>) =>
        fetcher<Room>(`/clinics/${clinicId}/rooms/${uuid}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    deleteRoom: (clinicId: string, uuid: string) =>
        fetcher(`/clinics/${clinicId}/rooms/${uuid}/`, {
            method: 'DELETE'
        }),

    // Medical Records
    getMedicalRecords: () => fetcher<MedicalRecord[]>('/medical-records/'),

    getMedicalRecord: (uuid: string) => fetcher<MedicalRecord>(`/medical-records/${uuid}/`),

    createMedicalRecord: (data: Partial<MedicalRecord>) =>
        fetcher<MedicalRecord>('/medical-records/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    updateMedicalRecord: (uuid: string, data: Partial<MedicalRecord>) =>
        fetcher<MedicalRecord>(`/medical-records/${uuid}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    // Appointments endpoints
    getAppointments: () => fetcher<Appointment[]>('/appointments/'),

    getAppointment: (uuid: string) => fetcher<Appointment>(`/appointments/${uuid}/`),

    createAppointment: (data: Partial<Appointment>) =>
        fetcher<Appointment>('/appointments/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    updateAppointment: (uuid: string, data: Partial<Appointment>) =>
        fetcher<Appointment>(`/appointments/${uuid}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    deleteAppointment: (uuid: string) =>
        fetcher(`/appointments/${uuid}/`, {
            method: 'DELETE'
        })
}

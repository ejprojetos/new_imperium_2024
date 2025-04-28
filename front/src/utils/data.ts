import type { Role } from '@/types/users.types'

export const academicFormations = [
    { id: 'ensino_medio', label: 'Ensino Médio' },
    { id: 'tecnico', label: 'Técnico' },
    { id: 'tecnologo', label: 'Tecnólogo' },
    { id: 'graduacao', label: 'Graduação' },
    { id: 'pos_graduacao', label: 'Pós-Graduação' },
    { id: 'mba', label: 'MBA' },
    { id: 'mestrado', label: 'Mestrado' },
    { id: 'doutorado', label: 'Doutorado' },
    { id: 'pos_doutorado', label: 'Pós-Doutorado' }
]

export const medicalSpecialties = [
    { id: 'alergologia', label: 'Alergologia' },
    { id: 'anestesiologia', label: 'Anestesiologia' },
    { id: 'angiologia', label: 'Angiologia' },
    { id: 'cardiologia', label: 'Cardiologia' },
    { id: 'cirurgia_cardiovascular', label: 'Cirurgia Cardiovascular' },
    { id: 'cirurgia_geral', label: 'Cirurgia Geral' },
    { id: 'cirurgia_plastica', label: 'Cirurgia Plástica' },
    { id: 'cirurgia_vascular', label: 'Cirurgia Vascular' },
    { id: 'clínica_médica', label: 'Clínica Médica' },
    { id: 'dermatologia', label: 'Dermatologia' },
    { id: 'endocrinologia', label: 'Endocrinologia' },
    { id: 'gastroenterologia', label: 'Gastroenterologia' },
    { id: 'geriatria', label: 'Geriatria' },
    { id: 'ginecologia_obstetricia', label: 'Ginecologia e Obstetrícia' },
    { id: 'hematologia', label: 'Hematologia' },
    { id: 'infectologia', label: 'Infectologia' },
    { id: 'medicina_do_trabalho', label: 'Medicina do Trabalho' },
    { id: 'medicina_esportiva', label: 'Medicina Esportiva' },
    { id: 'nefrologia', label: 'Nefrologia' },
    { id: 'neurologia', label: 'Neurologia' },
    { id: 'oftalmologia', label: 'Oftalmologia' },
    { id: 'oncologia', label: 'Oncologia' },
    { id: 'ortopedia', label: 'Ortopedia' },
    { id: 'otorrinolaringologia', label: 'Otorrinolaringologia' },
    { id: 'pediatria', label: 'Pediatria' },
    { id: 'psiquiatria', label: 'Psiquiatria' },
    { id: 'radiologia', label: 'Radiologia' },
    { id: 'reumatologia', label: 'Reumatologia' },
    { id: 'urologia', label: 'Urologia' }
]

export const weekDays = [
    {
        id: 'Segunda-feira',
        label: 'Segunda-feira'
    },
    {
        id: 'Terça-feira',
        label: 'Terça-feira'
    },
    {
        id: 'Quarta-feira',
        label: 'Quarta-feira'
    },
    {
        id: 'Quinta-feira',
        label: 'Quinta-feira'
    },
    {
        id: 'Sexta-feira',
        label: 'Sexta-feira'
    },
    {
        id: 'Sábado',
        label: 'Sábado'
    },
    {
        id: 'Domingo',
        label: 'Domingo'
    }
] as const

export const turns = [
    {
        id: 'Matutino',
        label: 'Matutino'
    },
    {
        id: 'Vespertino',
        label: 'Vespertino'
    },
    {
        id: 'Noturno',
        label: 'Noturno'
    }
] as const

export type ROLE = 'ADMIN' | 'RECEPTIONIST' | 'DOCTOR' | 'PATIENT'

export const roles: Record<ROLE, string> = {
    ADMIN: 'Administrador',
    DOCTOR: 'Médico',
    RECEPTIONIST: 'Recepcionista',
    PATIENT: 'Paciente'
}

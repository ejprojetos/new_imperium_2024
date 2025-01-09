import type { NavigationGuardNext, RouteLocationNormalized } from 'vue-router'

const publicRoutes = [
    '/auth/login',
    '/auth/esqueci-senha',
    '/auth/email-enviado',
    '/auth/redefinir-senha',
    '/auth/senha-redefinida',
    '/'
]

const userTypeRoutes = {
    admin: ['/dashboard/clinicas', '/dashboard/institucional'],
    medico: ['/dashboard/medicos', '/dashboard/consultas'],
    paciente: ['/dashboard/pacientes', '/dashboard/minhas-consultas'],
    recepcionista: ['/dashboard/recepcionistas', '/dashboard/consultas']
}

export function authGuard(
    to: RouteLocationNormalized,
    from: RouteLocationNormalized,
    next: NavigationGuardNext
) {
    const accessToken = localStorage.getItem('access_token')
    const authRequired = !publicRoutes.includes(to.path)

    if (authRequired && !accessToken) {
        return next('/auth/login')
    }

    if (accessToken && publicRoutes.includes(to.path)) {
        return next('/dashboard')
    }

    next()
}

export function roleGuard(allowedRoles: Array<'ADMIN' | 'DOCTOR' | 'PATIENT' | 'RECEPTIONIST'>) {
    return (
        to: RouteLocationNormalized,
        from: RouteLocationNormalized,
        next: NavigationGuardNext
    ) => {
        const userRole = localStorage.getItem('user_role') as
            | 'ADMIN'
            | 'DOCTOR'
            | 'PATIENT'
            | 'RECEPTIONIST'

        if (!userRole || !allowedRoles.includes(userRole)) {
            return next('/dashboard')
        }

        next()
    }
}

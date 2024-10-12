import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            // component: () => import('../views/institucional/index.vue'
            redirect: '/dashboard'
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/dashboard/index.vue')
        },
        {
            path: '/dashboard/institucional',
            name: 'institucional',
            component: () => import('../views/dashboard/institucional/index.vue')
        },
        {
            path: '/dashboard/institucional/secao-inicial',
            name: 'secao-inicial',
            component: () => import('../views/dashboard/institucional/secao-inicial.vue')
        },
        {
            path: '/dashboard/institucional/fluxo',
            name: 'fluxo',
            component: () => import('../views/dashboard/institucional/fluxo.vue')
        },
        {
            path: '/dashboard/consultas',
            name: 'consultas',
            component: () => import('../views/dashboard/consultas/consultas.vue')
        },
        {
            path: '/dashboard/recepcionistas',
            name: 'recepcionistas',
            component: () => import('../views/dashboard/recepcionistas/recepcionistas.vue')
        },
        {
            path: '/dashboard/medicos',
            name: 'medicos',
            component: () => import('../views/dashboard/medicos/medicos.vue')
        },
        {
            path: '/dashboard/pacientes',
            name: 'pacientes',
            component: () => import('../views/dashboard/pacientes/pacientes.vue')
        },
        {
            path: '/dashboard/institucional/features',
            name: 'features',
            component: () => import('../views/dashboard/institucional/features.vue')
        },
        {
            path: '/dashboard/institucional/depoimentos',
            name: 'depoimentos',
            component: () => import('../views/dashboard/institucional/depoimentos.vue')
        },
        {
            path: '/dashboard/institucional/cadastrar-depoimentos',
            name: 'cadastrar-depoimentos',
            component: () => import('../views/dashboard/institucional/cadastrar-depoimentos.vue')
        },
        {
            path: '/dashboard/clinicas',
            name: 'clinicas',
            component: () => import('../views/dashboard/clinicas/index.vue')
        },
        {
            path: '/dashboard/clinicas/cadastrar',
            name: 'cadastrar-clinica',
            component: () => import('../views/dashboard/clinicas/cadastrar-clinica.vue')
        },
        {
            path: '/dashboard/emails',
            name: 'emails',
            component: () => import('../views/dashboard/emails/index.vue')
        },
        {
            path: '/dashboard/emails/:id',
            name: 'cadastrar-email',
            component: () => import('../views/dashboard/emails/view-email.vue')
        },
        {
            path: '/:pathMatch(.*)*',
            name: '404',
            component: () => import('../views/404.vue')
        }
    ]
})

export default router

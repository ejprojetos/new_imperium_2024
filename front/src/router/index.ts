import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../views/institucional/index.vue'),
            // redirect: '/dashboard',
            children: []
        },
        {
            path: '/auth/login',
            name: 'login',
            component: () => import('../views/auth/login.vue')
        },
        {
            path: '/auth/esqueci-senha',
            name: 'esqueci-senha',
            component: () => import('../views/auth/esqueci-senha.vue')

        },
        {
            path: '/auth/email-enviado',
            name: 'email-enviado',
            component: () => import('../views/auth/email-enviado.vue')
        },
        {
            path: '/auth/redefinir-senha',
            name: 'redefinir-senha',
            component: () => import('../views/auth/redefinir-senha.vue')
        },
        {
            path: '/auth/senha-redefinida',
            name: 'senha-redefinida',
            component: () => import('../views/auth/senha-redefinida.vue')
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/dashboard/index.vue')
        },
        {
            path: '/dashboard/perfil/clinica',
            name: 'perfil_clinica',
            component: () => import('../views/dashboard/perfil/adm_clinica.vue')
        },
        {
            path: '/dashboard/perfil/administrador',
            name: 'perfil_administrador',
            component: () => import('../views/dashboard/perfil/adm_clinica.vue')
        },
        {
            path: '/dashboard/perfil/paciente',
            name: 'perfil_paciente',
            component: () => import('../views/dashboard/perfil/paciente.vue')
        },
        {
            path: '/dashboard/perfil/medico',
            name: 'perfil_medico',
            component: () => import('../views/dashboard/perfil/medico.vue')
        },
        {
            path: '/dashboard/perfil/recepcionista',
            name: 'perfil_recepcionista',
            component: () => import('../views/dashboard/perfil/recepcionista.vue')
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
            path: '/dashboard/minhas-consultas',
            name: 'minhas-consultas',
            component: () => import('../views/dashboard/consultas/minhas-consultas.vue')
        },
        {
            path: '/dashboard/recepcionistas',
            name: 'recepcionistas',
            component: () => import('../views/dashboard/recepcionistas/recepcionistas.vue')
        },
        {
            path: '/dashboard/recepcionistas/:id', // visualizar perfil de qualquer recepcionista na lista
            name: 'visualizar-recepcionista',
            component: () =>
                import('../views/dashboard/recepcionistas/visualizar-recepcionista.vue')
        },
        {
            path: '/dashboard/medicos',
            name: 'medicos',
            component: () => import('../views/dashboard/medicos/medicos.vue')
        },
        {
            path: '/dashboard/medicos/:id',
            name: 'visualizar-medico',
            component: () => import('../views/dashboard/medicos/visualizar-medico.vue')
        },
        {
            path: '/dashboard/medicos/cadastrar-consultas',
            name: 'cadastrar-consultas',
            component: () => import('../views/dashboard/medicos/cadastrar-consultas.vue')
        },
        {
            path: '/dashboard/medicos/editar-consultas',
            name: 'editar-consultas',
            component: () => import('../views/dashboard/medicos/editar-consultas.vue')
        },
        {
            path: '/dashboard/pacientes',
            name: 'pacientes',
            component: () => import('../views/dashboard/pacientes/pacientes.vue')
        },
        {
            path: '/dashboard/pacientes/:id',
            name: 'visualizar-paciente',
            component: () => import('../views/dashboard/pacientes/visualizar-paciente.vue')
        },
        {
            path: '/dashboard/pacientes/cadastrar-consulta',
            name: 'cadastrar-consulta',
            component: () => import('../views/dashboard/pacientes/cadastrar-consulta.vue')
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
        },
        {
            path: '/dashboard/recepcionista/cadastrar',
            name: 'cadastrar-recepcionista',
            component: () => import('../views/dashboard/recepcionistas/cadastrar-recepcionista.vue')
        },
        {
            path: '/dashboard/pacientes/cadastrar',
            name: 'cadastrar-paciente',
            component: () => import('../views/dashboard/pacientes/cadastrar-paciente.vue')
        },
        {
            path: '/dashboard/medicos/cadastrar',
            name: 'cadastrar-medico',
            component: () => import('../views/dashboard/medicos/cadastrar-medico.vue')
        },
        {
            path: '/dashboard/prontuario/:id',
            name: 'prontuario',
            component: () => import('../views/dashboard/prontuario/prontuario.vue')
        },
        {
            path: '/dashboard/suporte/escolher-perfil',
            name: 'escolher-perfil',
            component: () => import('../views/dashboard/suporte/escolher_perfil.vue')
        },
        {
            path: '/dashboard/suporte/manuais',
            name: 'manuais',
            component: () => import('../views/dashboard/suporte/manuais.vue')
        },
        {
            path: '/dashboard/suporte/politicas',
            name: 'politicas',
            component: () => import('../views/dashboard/suporte/politicas.vue')
        },
        {
            path: '/dashboard/suporte/politicas-usuario',
            name: 'politicas-usuario',
            component: () => import('../views/dashboard/suporte/politicas_usuario.vue')
        },
        {
            path: '/dashboard/suporte/administrador',
            name: 'suporte-administrador',
            component: () => import('../views/dashboard/suporte/suporte_administrador.vue')
        },
        {
            path: '/dashboard/suporte/faq',
            name: 'faq',
            component: () => import('../views/dashboard/suporte/faq.vue')
        },
        {
            path: '/dashboard/perfil/recepcionista/cadastrar-consulta',
            name: 'cadastrar-consulta',
            component: () => import('../views/dashboard/recepcionistas/cadastrar-consulta.vue')
        },
        {
            path: '/dashboard/perfil/recepcionista/cadastrar-consulta',
            name: 'cadastrar-consulta',
            component: () => import('../views/dashboard/recepcionistas/cadastrar-consulta.vue')
        }
    ]
})

export default router

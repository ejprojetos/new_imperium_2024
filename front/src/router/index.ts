import { createRouter, createWebHistory } from 'vue-router'
import { authGuard, roleGuard } from './guards'

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
            name: 'receptionist-details',
            component: () =>
                import(
                    '../views/dashboard/recepcionistas/receptionist-details/receptionist-details.vue'
                )
        },
        {
            path: '/dashboard/medicos',
            name: 'medicos',
            component: () => import('../views/dashboard/medicos/medicos.vue')
        },
        {
            path: '/dashboard/medicos/:id',
            name: 'doctor-details',
            component: () => import('../views/dashboard/medicos/doctor-details/doctor-details.vue')
        },
        {
            path: '/dashboard/medicos/cadastrar-consultas',
            name: 'cadastrar-consultas',
            component: () => import('../views/dashboard/consultas/cadastrar-consultas.vue')
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
            component: () => import('../views/dashboard/consultas/cadastrar-consultas.vue')
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
            path: '/dashboard/institucional/cadastrar-depoimentos/:id?',
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
            path: '/dashboard/clinicas/cadastrar/:id',
            name: 'editar-clinica',
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
            component: () => import('../views/dashboard/emails/view-email.vue'),
            props: true
        },
        {
            path: '/:pathMatch(.*)*',
            name: '404',
            component: () => import('../views/404.vue')
        },
        {
            path: '/dashboard/recepcionista/cadastrar',
            name: 'receptionist-registration',
            component: () =>
                import('../views/dashboard/recepcionistas/receptionist-registration/index.vue')
        },
        {
            path: '/dashboard/pacientes/cadastrar',
            name: 'pacient-registration',
            component: () => import('../views/dashboard/pacientes/patient-registration/index.vue')
        },
        {
            path: '/dashboard/medicos/cadastrar',
            name: 'doctor-registration',
            component: () => import('../views/dashboard/medicos/doctor-registration/index.vue')
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
            path: '/dashboard/suporte/editar-manuais',
            name: 'editar-manuais',
            component: () => import('../views/dashboard/suporte/editar-manuais.vue')
        },

        {
            path: '/dashboard/politicas/politicas',
            name: 'politicas',
            component: () => import('../views/dashboard/politicas/politicas.vue')
        },
        {
            path: '/dashboard/suporte/cadastrar-politicas',
            name: 'cadastrar-politicas',
            component: () => import('../views/dashboard/suporte/cadastrar-politicas.vue')
        },

        {
            path: '/dashboard/politicas/politicas-usuario',
            name: 'politicas-usuario',
            component: () => import('../views/dashboard/politicas/politicas_usuario.vue')
        },
        {
            path: '/dashboard/politicas/politicas-usuario-pag',
            name: 'politicas-usuario-pag',
            component: () => import('../views/dashboard/politicas/politicas_usuario_pag.vue')
        },
        {
            path: '/dashboard/politicas/politicas-publicacao',
            name: 'politicas-publicacao',
            component: () => import('../views/dashboard/politicas/politicas_publicacao.vue')
        },
        {
            path: '/dashboard/suporte/administrador',
            name: 'suporte-administrador',
            component: () => import('../views/dashboard/suporte/suporte_administrador.vue')
        },
        {
            path: '/dashboard/suporte/suporte-usuario',
            name: 'suporte-usuario',
            component: () => import('../views/dashboard/suporte/suporte_usuario.vue')
        },
        {
            path: '/dashboard/suporte/contatos',
            name: 'contatos',
            component: () => import('../views/dashboard/suporte/contatos.vue')
        },
        {
            path: '/dashboard/suporte/cadastrar-pergunta',
            name: 'cadastrar-pergunta',
            component: () => import('../views/dashboard/faqs/cadastrar_pergunta.vue')
        },
        {
            path: '/dashboard/suporte/editar-pergunta',
            name: 'editar-pergunta',
            component: () => import('../views/dashboard/faqs/editar_pergunta.vue')
        },
        {
            path: '/dashboard/suporte/faq',
            name: 'faq',
            component: () => import('../views/dashboard/faqs/faq.vue')
        },
        {
            path: '/dashboard/suporte/editar_faq',
            name: 'editar-faq',
            component: () => import('../views/dashboard/faqs/editar_faq.vue')
        },
        {
            path: '/dashboard/perfil/recepcionista/cadastrar-consulta',
            name: 'cadastrar-consulta-recepcionista',
            component: () => import('../views/dashboard/consultas/cadastrar-consultas.vue')
        }
    ]
})

router.beforeEach(authGuard)

router.beforeEach((to, from, next) => {
    switch (to.path) {
        case '/dashboard/clinicas':
        case '/dashboard/institucional':
            return roleGuard(['ADMIN'])(to, from, next)
        case '/dashboard/medicos':
        case '/dashboard/consultas/cadastrar':
            return roleGuard(['DOCTOR', 'ADMIN'])(to, from, next)
        case '/dashboard/recepcionistas':
            return roleGuard(['ADMIN', 'RECEPTIONIST'])(to, from, next)
        default:
            next()
    }
})

export default router

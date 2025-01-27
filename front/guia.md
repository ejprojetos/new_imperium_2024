1. Estrutura de Serviços
   1.1 Fetcher Service
   Primeiro, temos o serviço base para fazer requisições HTTP (fetcher.service.ts):

```ts
export const fetcher = <T>(url: string, options?: RequestInit): Promise<T> => {
    const baseURL = import.meta.env.VITE_API_URL

    const defaultOptions: RequestInit = {
        headers: {
            'Content-Type': 'application/json'
        }
    }

    return fetch(`${baseURL}${url}`, {
        ...defaultOptions,
        ...options
    }).then((res) => res.json())
}
```

1.2 Serviços Específicos
Para cada entidade, crie um serviço específico. Exemplo para clínicas:

```ts
import { fetcher } from './fetcher.service'
import type { Clinic } from '@/types/clinic.types'

export const clinicService = {
    createClinic: (data: Partial<Clinic>) =>
        fetcher<Clinic>('/clinics/', {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    getClinic: (id: string) => fetcher<Clinic>(`/clinics/${id}/`),

    updateClinic: (id: string, data: Partial<Clinic>) =>
        fetcher<Clinic>(`/clinics/${id}/`, {
            method: 'PATCH',
            body: JSON.stringify(data)
        }),

    deleteClinic: (id: string) =>
        fetcher(`/clinics/${id}/`, {
            method: 'DELETE'
        })
}
```

2. Tipos TypeScript
   Defina interfaces para seus dados:

```ts
export interface Clinic {
    id: string
    name: string
    cnpj: string
    is_active: boolean
    address: {
        country: string
        state: string
        city: string
        neighborhood: string
        zipCode: string
        street: string
        number: string
    }
}
```

3. Store (Pinia)
   Use Pinia para gerenciar o estado:

```ts
import { defineStore } from 'pinia'
import { clinicService } from '@/services/clinic.service'
import type { Clinic } from '@/types/clinic.types'

export const useClinicStore = defineStore('clinic', () => {
    const clinics = ref<Clinic[]>([])

    async function createClinic(data: Partial<Clinic>) {
        try {
            const response = await clinicService.createClinic(data)
            clinics.value.push(response)
            return response
        } catch (error) {
            console.error('Error creating clinic:', error)
            throw error
        }
    }

    return {
        clinics,
        createClinic
    }
})
```

4. Uso nos Componentes
   Exemplo de como usar em um componente Vue:

```vue
<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useClinicStore } from '@/stores/clinic/clinic.store'
import type { Clinic } from '@/types/clinic.types'
import { toast } from 'vue-sonner'

const clinicStore = useClinicStore()

const formData = reactive({
    clinicName: '',
    cnpj: ''
    // ... outros campos
})

const submitForm = async () => {
    try {
        const clinicData = {
            name: formData.clinicName,
            cnpj: formData.cnpj
            // ... outros campos formatados
        }

        await clinicStore.createClinic(clinicData)
        toast.success('Clínica cadastrada com sucesso!')
    } catch (error) {
        toast.error('Erro ao cadastrar clínica')
        console.error(error)
    }
}
</script>
```

5. Configuração do Ambiente
   Crie um arquivo .env na raiz do projeto:

```
VITE_API_URL= http://191.252.192.82/api ou http://localhost:8000/api
```

O ip 172.105.155.145 é o ip do servidor da EJECT backend

6. Autenticação
   Para autenticar no backend, use o token de autenticação.

```ts
const token = localStorage.getItem('token')
const headers = token ? { Authorization: `Bearer ${token}` } : {}
```

7. Exemplo de post para criação de uma clínica em um dos componentes

```ts
const submitForm = async () => {
    try {
        const clinicData = formatClinicData()
        await clinicStore.createClinic(clinicData)
        toast.success('Clínica cadastrada com sucesso!')
        router.push('/dashboard/clinicas')
    } catch (error) {
        toast.error('Erro ao cadastrar clínica')
        console.error(error)
    }
}
```

8. Resumindo para criar uma nova integração

-   Criar os tipos TypeScript
-   Criar o serviço específico
-   Criar o store
-   Integrar ao componente

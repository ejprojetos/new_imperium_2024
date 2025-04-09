<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { fetcher } from '@/services/fetcher.service'
import { useUserStore } from '@/stores/user/useUserStore'
import { storeToRefs } from 'pinia'
import { QueryClient, useMutation, useQuery } from '@tanstack/vue-query'
import { getInitials } from '@/lib/utils'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import type { User } from '@/types/users.types'
import { roles, type ROLE } from '@/utils/data'
import { ContactData, AddressData } from '@/components/commons'
import { Card, CardContent } from '@/components/ui/card'
import { AdminData } from './form'
import { adminDataSchema, type AdminDataSchema } from './schema'
import { useForm } from 'vee-validate'
import { computed, ref, watch } from 'vue'
import { Button } from '@/components/ui/button'
import { toast } from '@/components/ui/toast'

const queryClient = new QueryClient()
const userStore = useUserStore()
const { id } = storeToRefs(userStore)

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo) => {
        return await fetcher<User>(`/users/${id.value}/`, {
            method: 'PATCH',
            body: JSON.stringify(newTodo)
        })
    }
})

const { data, isLoading } = useQuery<User, Error>({
    queryKey: ['user', id.value],
    queryFn: async () => {
        const response = await fetcher<User>(`/users/${id.value}`)
        if (!response) throw new Error('User not found')
        return response
    },
    staleTime: Infinity
})

// const { data: clinicData, isLoading: clinicIsLoading } = useQuery({
//     queryKey: ['clinic', id.value],
//     queryFn: async () => {
//         const response = await fetcher<Clinic>(`/clinic/${id.value}`)
//         if (!response) throw new Error('User not found')
//         return response
//     },
//     staleTime: Infinity
// })

function formatData(raw = data.value!): AdminDataSchema {
    if (!raw) {
        return {
            fullname: '',
            cpf: '',
            address: {
                zipCode: '',
                country: '',
                state: '',
                city: '',
                neighborhood: '',
                street: '',
                number: ''
            },
            email: '',
            phone: ''
        }
    }

    const admin = raw
    return {
        fullname: raw.first_name,
        cpf: raw.cpf,
        address: {
            zipCode: admin.address.zip_code,
            country: admin.address.country,
            state: admin.address.state,
            city: admin.address.city,
            neighborhood: admin.address.neighborhood,
            street: admin.address.street,
            number: admin.address.number
        },
        email: admin.email,
        phone: admin.phone
    }
}

const savedValues = ref<AdminDataSchema>({} as AdminDataSchema)

const initialValues = computed(() => {
    return formatData()
})

const { isFieldDirty, handleSubmit, setValues, resetForm } = useForm<AdminDataSchema>({
    validationSchema: adminDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: !!data.value
})

watch(initialValues, (newAsyncData) => {
    savedValues.value = formatData()
    setValues(newAsyncData)
})

const onSubmit = handleSubmit((values) => {
    const hasChanged = <K extends keyof AdminDataSchema>(
        key: K,
        subKey?: keyof AdminDataSchema[K]
    ) => {
        if (
            subKey &&
            typeof values[key] === 'object' &&
            typeof savedValues.value[key] === 'object'
        ) {
            return (values[key] as any)[subKey] !== (savedValues.value[key] as any)[subKey]
        }
        return values[key] !== savedValues.value[key]
    }

    const addressChanged =
        hasChanged('address', 'zipCode') ||
        hasChanged('address', 'country') ||
        hasChanged('address', 'state') ||
        hasChanged('address', 'city') ||
        hasChanged('address', 'street') ||
        hasChanged('address', 'number')

    const newData = {
        first_name: hasChanged('fullname') ? values.fullname : undefined,
        cpf: hasChanged('cpf') ? values.cpf : undefined,
        address: addressChanged
            ? {
                  zip_code: hasChanged('address', 'zipCode') ? values.address.zipCode : undefined,
                  country: hasChanged('address', 'country') ? values.address.country : undefined,
                  state: hasChanged('address', 'state') ? values.address.state : undefined,
                  city: hasChanged('address', 'city') ? values.address.city : undefined,
                  street: hasChanged('address', 'street') ? values.address.street : undefined,
                  number: hasChanged('address', 'number') ? values.address.number : undefined
              }
            : undefined,
        email: hasChanged('email') ? values.email : undefined,
        phone: hasChanged('phone') ? values.phone : undefined
    }

    mutate(newData as any, {
        onSuccess: async (newValue) => {
            if (newValue) {
                toast({
                    variant: 'success',
                    description: 'Administrador atualizado com sucesso! 🎉'
                })

                queryClient.setQueryData(['user', id], newValue)

                savedValues.value = formatData(newValue)
            }
        },
        onError: () => {
            toast({
                variant: 'destructive',
                description: 'Erro ao atualizar administrador! 😢'
            })
        }
    })
})
</script>

<template>
    <LayoutDashboard>
        <div v-if="isLoading" class="flex justify-center items-center h-full">
            <Loader class="animate-spin text-zinc-400 size-4" />
        </div>

        <form v-else-if="data" class="max-w-3xl mx-auto my-10" @submit="onSubmit">
            <div class="flex items-center justify-between mb-4">
                <div class="flex gap-4 items-center">
                    <Avatar size="base" class="bg-primary text-white">
                        <AvatarImage src="https://github.com/josmartrigueiro.pnag" alt="@unovue" />
                        <AvatarFallback>
                            {{ getInitials(data.first_name) }}
                        </AvatarFallback>
                    </Avatar>
                    <div>
                        <h2 class="text-3xl font-bold">
                            {{ data.first_name }}
                        </h2>
                        <div class="text-sm text-gray-500">
                            {{ roles[data.roles[0].name as ROLE] }}
                        </div>
                    </div>
                </div>
            </div>
            <Card>
                <CardContent class="p-6 space-y-6">
                    <AdminData :isFieldDirty="isFieldDirty" />
                    <AddressData :isFieldDirty="isFieldDirty" />
                    <ContactData :isFieldDirty="isFieldDirty" />
                </CardContent>
            </Card>

            <div class="mt-6 space-x-2 flex justify-end">
                <Button variant="outline" type="button">Cancelar</Button>
                <Button type="submit">
                    <!-- <Loader v-if="isPending" class="animate-spin size-4" /> -->
                    Salvar
                </Button>
            </div>
        </form>
    </LayoutDashboard>
</template>

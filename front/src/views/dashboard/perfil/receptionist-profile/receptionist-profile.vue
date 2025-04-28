<script setup lang="ts">
import { fetcher } from '@/services/fetcher.service'
import { useUserStore } from '@/stores/user/useUserStore'
import { storeToRefs } from 'pinia'
import { QueryClient, useMutation, useQuery } from '@tanstack/vue-query'
import { arraysHaveSameValues, getInitials } from '@/lib/utils'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import type { Recepcionist } from '@/types/users.types'
import { roles, type ROLE } from '@/utils/data'
import { ContactData, AddressData } from '@/components/commons'
import { Card, CardContent } from '@/components/ui/card'
import { useForm } from 'vee-validate'
import { computed, ref, watch } from 'vue'
import { Button } from '@/components/ui/button'
import { toast } from '@/components/ui/toast'
import PersonalData from '@/components/commons/personal-data.vue'
import { Loader } from 'lucide-vue-next'
import { ReceptionistData } from './form/index'
import type { ReceptionistDataSchema } from './schema'
import { receptionistDataSchema } from './schema'

const queryClient = new QueryClient()
const userStore = useUserStore()
const { id } = storeToRefs(userStore)

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo) => {
        return await fetcher<Recepcionist>(`/users/${id.value}/`, {
            method: 'PATCH',
            body: JSON.stringify(newTodo)
        })
    }
})

const { data } = useQuery<Recepcionist, Error>({
    queryKey: ['user', id],
    queryFn: async () => {
        const response = await fetcher<Recepcionist>(`/users/${id.value}`)
        if (!response) throw new Error('User not found')
        return response
    },
    staleTime: Infinity
})

function formatData(raw: Recepcionist = data.value!) {
    if (!raw) {
        return {}
    }
    if (!raw.availableForShift) {
        raw.availableForShift = false
    }

    const formatDate = raw.date_birth?.split('-')

    return {
        fullname: raw.first_name,
        cpf: raw.cpf,
        dateOfBirth: formatDate && `${formatDate[2]}/${formatDate[1]}/${formatDate[0]}`,
        gender: raw.gender as 'Masculino' | 'Feminino' | 'Outro',
        address: {
            zipCode: raw.address.zip_code,
            country: raw.address.country,
            state: raw.address.state,
            city: raw.address.city,
            neighborhood: raw.address.street,
            street: raw.address.street,
            number: raw.address.number
        },
        email: raw.email,
        phone: raw.phone,
        workDays: raw.expedient?.days_of_week || [],
        turns: raw.expedient?.turns || [],
        availableForShift: (raw.availableForShift ? 'yes' : 'no') as 'yes' | 'no'
    }
}

const initialValues = computed(() => {
    return formatData()
})

const savedValues = ref(formatData())

const { isFieldDirty, handleSubmit, setValues } = useForm<ReceptionistDataSchema>({
    validationSchema: receptionistDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: !!data.value
})

watch(initialValues, (newAsyncData) => {
    savedValues.value = formatData()
    setValues(newAsyncData)
})

const onSubmit = handleSubmit((values) => {
    const hasChanged = <K extends keyof ReceptionistDataSchema>(
        key: K,
        subKey?: keyof ReceptionistDataSchema[K]
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

    const formatDate = values.dateOfBirth.split('/')
    const addressChanged =
        hasChanged('address', 'zipCode') ||
        hasChanged('address', 'country') ||
        hasChanged('address', 'state') ||
        hasChanged('address', 'city') ||
        hasChanged('address', 'street') ||
        hasChanged('address', 'number')

    const expedientChanged =
        !arraysHaveSameValues({
            defaultData: savedValues.value.workDays,
            newData: values.workDays
        }) ||
        !arraysHaveSameValues({
            defaultData: savedValues.value.turns,
            newData: values.turns
        })

    const newData = {
        first_name: hasChanged('fullname') ? values.fullname : undefined,
        cpf: hasChanged('cpf') ? values.cpf : undefined,
        date_birth: hasChanged('dateOfBirth')
            ? `${formatDate[2]}-${formatDate[1]}-${formatDate[0]}`
            : undefined,
        gender: hasChanged('gender') ? values.gender : undefined,
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
        phone: hasChanged('phone') ? values.phone : undefined,
        expedient: expedientChanged
            ? {
                  days_of_week: !arraysHaveSameValues({
                      defaultData: savedValues.value.workDays,
                      newData: values.workDays
                  })
                      ? values.workDays
                      : undefined,
                  turns: !arraysHaveSameValues({
                      defaultData: savedValues.value.turns,
                      newData: values.turns
                  })
                      ? values.turns
                      : undefined
              }
            : undefined,
        availableForShift: hasChanged('availableForShift')
            ? values.availableForShift === 'yes'
            : undefined
    }

    mutate(newData as any, {
        onSuccess: async (newValue) => {
            if (newValue) {
                toast({
                    variant: 'success',
                    description: 'Recepcionista atualizado com sucesso! 🎉'
                })

                queryClient.setQueryData(['receptionist-user', id], newValue)

                savedValues.value = formatData(newValue)
            }
        },
        onError: () => {
            toast({
                variant: 'destructive',
                description: 'Erro ao atualizar recepcionista! 😢'
            })
        }
    })
})
</script>

<template>
    <form class="max-w-3xl mx-auto my-10" @submit="onSubmit">
        <div class="flex items-center justify-between mb-4">
            <div class="flex gap-4 items-center">
                <Avatar size="base" class="bg-primary text-white">
                    <AvatarImage src="https://github.com/josmartrigueiro.pnag" alt="@unovue" />
                    <AvatarFallback>
                        {{ getInitials(data?.first_name ?? '') }}
                    </AvatarFallback>
                </Avatar>
                <div>
                    <h2 class="text-3xl font-bold">
                        {{ data?.first_name }}
                    </h2>
                    <div class="text-sm text-gray-500">
                        {{ roles[data?.roles[0].name as ROLE] }}
                    </div>
                </div>
            </div>
        </div>
        <Card>
            <CardContent class="p-6 space-y-6">
                <PersonalData :isFieldDirty="isFieldDirty" />
                <AddressData :isFieldDirty="isFieldDirty" />
                <ContactData :isFieldDirty="isFieldDirty" />
                <ReceptionistData :isFieldDirty="isFieldDirty" />
            </CardContent>
        </Card>

        <div class="mt-6 space-x-2 flex justify-end">
            <Button variant="outline" type="button">Cancelar</Button>
            <Button type="submit">
                <Loader v-if="isPending" class="animate-spin size-4" />
                Salvar
            </Button>
        </div>
    </form>
</template>

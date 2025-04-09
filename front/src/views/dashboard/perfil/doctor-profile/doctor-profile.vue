<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { fetcher } from '@/services/fetcher.service'
import { useUserStore } from '@/stores/user/useUserStore'
import { storeToRefs } from 'pinia'
import { QueryClient, useMutation, useQuery } from '@tanstack/vue-query'
import { getInitials } from '@/lib/utils'
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import type { Doctor, Recepcionist } from '@/types/users.types'
import { roles, type ROLE } from '@/utils/data'
import { ContactData, AddressData, DoctorProfessionalData } from '@/components/commons'
import { Card, CardContent } from '@/components/ui/card'
import { useForm } from 'vee-validate'
import { computed, ref, watch } from 'vue'
import { Button } from '@/components/ui/button'
import { toast } from '@/components/ui/toast'
import PersonalData from '@/components/commons/personal-data.vue'
import { Loader } from 'lucide-vue-next'
import type { DoctorDataSchema } from './schema'
import { doctorDataSchema } from './schema'

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

const { data, isLoading } = useQuery<Doctor, Error>({
    queryKey: ['doctor-user', id],
    queryFn: async () => {
        const response = await fetcher<Doctor>(`/users/${id.value}`)
        if (!response) throw new Error('User not found')
        return response
    },
    staleTime: Infinity
})

function formatData(raw: Doctor = data.value!) {
    if (!raw) {
        return {}
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
        attachDocument: raw.attach_document ?? null,
        formation: raw.formacao,
        specialty: raw.speciality,
        crm: raw.crm
    }
}

const initialValues = computed(() => {
    return formatData()
})

const savedValues = ref(formatData())

const { isFieldDirty, handleSubmit, setValues, values, resetForm } = useForm<DoctorDataSchema>({
    validationSchema: doctorDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: !!data.value
})

watch(initialValues, (newAsyncData) => {
    savedValues.value = formatData()
    setValues(newAsyncData)
})

const onSubmit = handleSubmit(async (values) => {
    const hasChanged = <K extends keyof DoctorDataSchema>(
        key: K,
        subKey?: keyof DoctorDataSchema[K]
    ) => {
        if (
            subKey &&
            typeof values[key] === 'object' &&
            typeof savedValues.value?.[key as keyof typeof savedValues.value] === 'object'
        ) {
            // @ts-ignore
            return (values[key] as any)[subKey] !== (savedValues.value[key] as any)[subKey]
        }
        return (
            values[key as keyof typeof values] !==
            savedValues.value?.[key as keyof typeof savedValues.value]
        )
    }

    const formatDate = values.dateOfBirth.split('/')
    let base64Image: string | null = null

    if (values.file) {
        base64Image = await new Promise((resolve) => {
            const reader = new FileReader()
            reader.readAsDataURL(values.file as File)
            reader.onload = () => resolve(reader.result as string)
        })
    }

    const addressChanged =
        hasChanged('address', 'zipCode') ||
        hasChanged('address', 'country') ||
        hasChanged('address', 'state') ||
        hasChanged('address', 'city') ||
        hasChanged('address', 'street') ||
        hasChanged('address', 'number') ||
        hasChanged('address', 'neighborhood')

    const newData: Partial<Doctor> = {
        first_name: hasChanged('fullname') ? values.fullname : undefined,
        cpf: hasChanged('cpf') ? values.cpf : undefined,
        date_birth: hasChanged('dateOfBirth')
            ? `${formatDate[2]}-${formatDate[1]}-${formatDate[0]}`
            : undefined,
        gender: hasChanged('gender') ? values.gender : undefined,
        // @ts-ignore
        address: addressChanged
            ? {
                  zip_code: hasChanged('address', 'zipCode') ? values.address.zipCode : undefined,
                  country: hasChanged('address', 'country') ? values.address.country : undefined,
                  state: hasChanged('address', 'state') ? values.address.state : undefined,
                  city: hasChanged('address', 'city') ? values.address.city : undefined,
                  street: hasChanged('address', 'street') ? values.address.street : undefined,
                  number: hasChanged('address', 'number') ? values.address.number : undefined,
                  neighborhood: hasChanged('address', 'neighborhood')
                      ? values.address.neighborhood
                      : undefined
              }
            : undefined,
        email: hasChanged('email') ? values.email : undefined,
        phone: hasChanged('phone') ? values.phone : undefined,
        formacao: hasChanged('formation') ? values.formation : undefined,
        crm: hasChanged('crm') ? values.crm.toUpperCase() : undefined,
        attach_document: base64Image
            ? base64Image
            : values.attachDocument === null
              ? null
              : undefined
    }

    mutate(newData as any, {
        onSuccess: async (newValue) => {
            if (newValue) {
                toast({
                    variant: 'success',
                    description: 'Dados atualizados com sucesso! 🎉'
                })

                queryClient.setQueryData(['doctor-user', id], newValue)
            }
        },
        onError: () => {
            toast({
                variant: 'destructive',
                description: 'Erro ao atualizar os dados! 😢'
            })
        }
    })
})

function handleResetDocument() {
    setValues({
        file: undefined,
        attachDocument: undefined
    })
}
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
                    <PersonalData :isFieldDirty="isFieldDirty" />
                    <AddressData :isFieldDirty="isFieldDirty" />
                    <ContactData :isFieldDirty="isFieldDirty" />
                    <DoctorProfessionalData
                        :isEditMode="true"
                        :onResetDocumentImg="handleResetDocument"
                        :isFieldDirty="isFieldDirty"
                        :imageUrl="values.attachDocument" />
                </CardContent>
            </Card>

            <div class="mt-6 space-x-2 flex justify-end">
                <Button variant="outline" type="button" @click="resetForm">Cancelar</Button>
                <Button type="submit">
                    <Loader v-if="isPending" class="animate-spin size-4" />
                    Salvar
                </Button>
            </div>
        </form>
    </LayoutDashboard>
</template>

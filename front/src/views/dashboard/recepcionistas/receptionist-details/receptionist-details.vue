<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { ref, computed, watch } from 'vue'

import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

import PersonalData from './form/personal-data.vue'
import WorkSchedule from './form/work-schedule.vue'
import { Button } from '@/components/ui/button'
import type { Recepcionist } from '@/types/users.types'
import { Loader } from 'lucide-vue-next'

import { useForm } from 'vee-validate'
import { receptionistDataSchema, type ReceptionistDataSchema } from './schema'
import { useQuery, useMutation } from '@tanstack/vue-query'
import { useRoute } from 'vue-router'
import { fetcher } from '@/services/fetcher.service'
import { useToast } from '@/components/ui/toast/use-toast'
import { getInitials } from '@/lib/utils'
import RemoveReceptionistDialog from './remove-receptionist-dialog.vue'

const { toast } = useToast()
const router = useRoute()
const receptionistId = router.params.id as string

const id = ref(receptionistId)
const isEditMode = ref(false)

const { data, isLoading } = useQuery({
    queryKey: ['receptionist-user', id],
    queryFn: async () => await fetcher<Recepcionist>(`/users/${receptionistId}`)
})

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo) => {
        return await fetcher<Recepcionist>(`/users/${receptionistId}/`, {
            method: 'PATCH',
            body: JSON.stringify(newTodo)
        })
    }
})

const initialValues = computed(() => {
    const formatDate = data.value?.date_birth.split('-')

    return {
        fullname: data.value?.first_name,
        cpf: data.value?.cpf,
        dateOfBirth: formatDate && `${formatDate[2]}/${formatDate[1]}/${formatDate[0]}`,
        gender: data.value?.gender as 'Masculino' | 'Feminino' | 'Outro',
        address: {
            zipCode: data.value?.address.zip_code,
            country: data.value?.address.country,
            state: data.value?.address.state,
            city: data.value?.address.city,
            neighborhood: data.value?.address.street,
            street: data.value?.address.street,
            number: data.value?.address.number
        },
        email: data.value?.email,
        phone: data.value?.phone,
        workDays: data.value?.expedient?.days_of_week || [],
        turns: data.value?.expedient?.turns || [],
        availableForShift: (data.value?.availableForShift ? 'yes' : 'no') as 'yes' | 'no'
    }
})

const { isFieldDirty, handleSubmit, setValues, resetForm } = useForm<ReceptionistDataSchema>({
    validationSchema: receptionistDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: true
})

watch(initialValues, (newAsyncData) => {
    setValues(newAsyncData)
})

const onSubmit = handleSubmit((values) => {
    console.log(values.workDays, initialValues.value.workDays)

    const hasChanged = <K extends keyof ReceptionistDataSchema>(
        key: K,
        subKey?: keyof ReceptionistDataSchema[K]
    ) => {
        if (
            subKey &&
            typeof values[key] === 'object' &&
            typeof initialValues.value[key] === 'object'
        ) {
            return (values[key] as any)[subKey] !== (initialValues.value[key] as any)[subKey]
        }
        return values[key] !== initialValues.value[key]
    }

    const formatDate = values.dateOfBirth.split('/')

    const newData = {
        first_name: hasChanged('fullname') ? values.fullname : undefined,
        cpf: hasChanged('cpf') ? values.cpf : undefined,
        date_birth: hasChanged('dateOfBirth')
            ? `${formatDate[2]}-${formatDate[1]}-${formatDate[0]}`
            : undefined,
        gender: hasChanged('gender') ? values.gender : undefined,
        address: {
            zip_code: hasChanged('address', 'zipCode') ? values.address.zipCode : undefined,
            country: hasChanged('address', 'country') ? values.address.country : undefined,
            state: hasChanged('address', 'state') ? values.address.state : undefined,
            city: hasChanged('address', 'city') ? values.address.city : undefined,
            street: hasChanged('address', 'street') ? values.address.street : undefined,
            number: hasChanged('address', 'number') ? values.address.number : undefined
        },
        email: hasChanged('email') ? values.email : undefined,
        phone: hasChanged('phone') ? values.phone : undefined,
        expedient: {
            days_of_week: hasChanged('workDays') ? values.workDays : undefined,
            turns: hasChanged('turns') ? values.turns : undefined
        },
        availableForShift: hasChanged('availableForShift')
            ? values.availableForShift === 'yes'
            : undefined
    }

    const isEmpty = Object.values(newData).every((value) => value === undefined)

    if (isEmpty) {
        isEditMode.value = false

        return
    }

    mutate(newData as any, {
        onSuccess: () => {
            toast({
                variant: 'success',
                description: 'Recepcionista atualizado com sucesso! 🎉'
            })
        },
        onError: () => {
            toast({
                variant: 'destructive',
                description: 'Erro ao atualizar recepcionista! 😢'
            })
        }
    })

    isEditMode.value = false
})

function handleCancel() {
    resetForm({
        values: initialValues.value
    })
    isEditMode.value = false
}
</script>

<template>
    <LayoutDashboard>
        <div v-if="isLoading" class="flex justify-center items-center h-full">
            <Loader class="animate-spin text-gray-400" />
        </div>
        <form v-else-if="data" class="max-w-3xl mx-auto my-10" @submit="onSubmit">
            <div class="flex items-center justify-between mb-4">
                <div class="flex gap-4 items-center">
                    <Avatar size="base" class="bg-primary text-white">
                        <AvatarImage src="https://github.com/josmartrigueiro.pnag" alt="@unovue" />
                        <AvatarFallback>
                            {{ initialValues.fullname && getInitials(initialValues.fullname) }}
                        </AvatarFallback>
                    </Avatar>
                    <div>
                        <h2 class="text-3xl font-bold">
                            {{ data?.first_name }}
                        </h2>
                        <div class="text-sm text-gray-500">Recepcionista</div>
                    </div>
                </div>
            </div>

            <Tabs default-value="personal">
                <TabsList
                    className="grid grid-cols-2 mb-4 border rounded-md p-1.5 border-gray-200 bg-white">
                    <TabsTrigger value="personal">Dados Pessoais</TabsTrigger>
                    <TabsTrigger value="work">Expediente</TabsTrigger>
                </TabsList>

                <TabsContent value="personal">
                    <PersonalData :isEditMode="isEditMode" :isFieldDirty="isFieldDirty" />
                </TabsContent>
                <TabsContent value="work">
                    <WorkSchedule :isEditMode="isEditMode" :isFieldDirty="isFieldDirty" />
                </TabsContent>
            </Tabs>

            <div class="mt-6 space-x-2 flex justify-end">
                <template v-if="!isEditMode">
                    <RemoveReceptionistDialog />
                    <Button @click="isEditMode = !isEditMode">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="16"
                            height="16"
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            class="lucide lucide-pencil">
                            <path
                                d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z" />
                            <path d="m15 5 4 4" />
                        </svg>
                        Editar
                    </Button>
                </template>
                <template v-if="isEditMode">
                    <Button
                        variant="outline"
                        type="button"
                        @click="handleCancel"
                        :disabled="isPending">
                        Cancelar
                    </Button>
                    <Button type="submit" :disabled="isPending">
                        <Loader v-if="isPending" class="animate-spin size-4" />
                        Salvar
                    </Button>
                </template>
            </div>
        </form>
    </LayoutDashboard>
</template>

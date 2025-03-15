<script setup lang="ts">
// Layout and Core Vue imports
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

// UI Components
import { Button } from '@/components/ui/button'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Loader } from 'lucide-vue-next'

// Form Components
import PersonalData from './form/personal-data.vue'
import WorkSchedule from './form/work-schedule.vue'
import RemoveReceptionistDialog from './remove-receptionist-dialog.vue'

// Types and Schemas
import type { Recepcionist } from '@/types/users.types'
import { receptionistDataSchema, type ReceptionistDataSchema } from './schema'

// Utilities and Services
import { useForm } from 'vee-validate'
import { useQuery, useMutation, QueryClient } from '@tanstack/vue-query'
import { fetcher } from '@/services/fetcher.service'
import { useToast } from '@/components/ui/toast/use-toast'
import { getInitials, arraysHaveSameValues } from '@/lib/utils'

const router = useRoute()
const { toast } = useToast()

const receptionistId = router.params.id as string
const id = ref(receptionistId)
const isEditMode = ref(false)
const queryClient = new QueryClient()

const { data, isLoading } = useQuery({
    queryKey: ['receptionist-user', id],
    queryFn: async () => await fetcher<Recepcionist>(`/users/${receptionistId}`),
    staleTime: 5 * 1000
})

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo) => {
        return await fetcher<Recepcionist>(`/users/${receptionistId}/`, {
            method: 'PATCH',
            body: JSON.stringify(newTodo)
        })
    }
})

function formatData(raw: Recepcionist = data.value!) {
    const formatDate = raw.date_birth.split('-')

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

const headerPersonalInfos = ref({
    fullName: initialValues.value?.fullname,
    initials: initialValues.value?.fullname && getInitials(initialValues.value.fullname)
})

const savedValues = ref(formatData())

const { isFieldDirty, handleSubmit, setValues, resetForm } = useForm<ReceptionistDataSchema>({
    validationSchema: receptionistDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: true
})

watch(initialValues, (newAsyncData) => {
    headerPersonalInfos.value.fullName = newAsyncData.fullname
    headerPersonalInfos.value.initials = getInitials(newAsyncData.fullname ?? '')

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
            defaultData: initialValues.value.workDays,
            newData: values.workDays
        }) ||
        !arraysHaveSameValues({
            defaultData: initialValues.value.turns,
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
                      defaultData: initialValues.value.workDays,
                      newData: values.workDays
                  })
                      ? values.workDays
                      : undefined,
                  turns: !arraysHaveSameValues({
                      defaultData: initialValues.value.turns,
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

    const isEmpty = Object.values(newData).every((value) => value === undefined)

    if (isEmpty) {
        isEditMode.value = false

        return
    }

    mutate(newData as any, {
        onSuccess: async (newData) => {
            if (newData) {
                toast({
                    variant: 'success',
                    description: 'Recepcionista atualizado com sucesso! 🎉'
                })

                if (headerPersonalInfos.value) {
                    headerPersonalInfos.value.fullName =
                        newData.first_name ?? headerPersonalInfos.value.fullName
                    headerPersonalInfos.value.initials = newData.first_name
                        ? getInitials(newData.first_name)
                        : headerPersonalInfos.value.initials
                    newData?.first_name && getInitials(newData.first_name)
                }

                queryClient.setQueryData(['receptionist-user', id], newData)

                savedValues.value = formatData(newData)
            }
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
                            {{ headerPersonalInfos.initials }}
                        </AvatarFallback>
                    </Avatar>
                    <div>
                        <h2 class="text-3xl font-bold">
                            {{ headerPersonalInfos.fullName }}
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

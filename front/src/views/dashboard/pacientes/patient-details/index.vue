<script setup lang="ts">
import PersonalData from './form/personal-data.vue'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Button } from '@/components/ui/button'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { getInitials } from '@/lib/utils'
import { fetcher } from '@/services/fetcher.service'
import type { Patient } from '@/types/users.types'
import { QueryClient, useMutation, useQuery } from '@tanstack/vue-query'
import { Loader } from 'lucide-vue-next'
import { useForm } from 'vee-validate'
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { patientDataSchema, type PatientDataSchema } from './schema'
import { useToast } from '@/components/ui/toast'
import DeleteUserDialog from '@/components/delete-user-dialog.vue'
import { useDeleteUserMutation } from '@/hooks/use-delete-user-mutation'

const route = useRoute()
const router = useRouter()
const isEditMode = ref(false)
const patientId = route.params.id as string

const id = ref(patientId)

const { toast } = useToast()

const queryClient = new QueryClient()

const { isPending, mutate } = useMutation({
    mutationFn: async (newData) => {
        return await fetcher<Patient>(`/users/${patientId}/`, {
            method: 'PATCH',
            body: JSON.stringify(newData)
        })
    }
})

const { mutate: deleteUserMutate, isPending: isPendingUser } = useDeleteUserMutation()

const { data, isLoading, error } = useQuery({
    queryKey: ['patient-user', id],
    queryFn: async () => await fetcher<Patient>(`/users/${patientId}`),
    staleTime: 5 * 1000
})

function formatData(raw: Patient = data.value!) {
    if (!raw) {
        return {}
    }

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
        attachDocument: raw.attach_document ?? null,
        formation: raw.formacao,
        crm: raw.crm
    }
}

const savedValues = ref(formatData())

const initialValues = computed(() => {
    return formatData()
})

const headerPersonalInfos = ref({
    fullName: initialValues.value?.fullname,
    initials: initialValues.value?.fullname && getInitials(initialValues.value.fullname)
})

const { isFieldDirty, handleSubmit, setValues, resetForm, errors } = useForm<PatientDataSchema>({
    validationSchema: patientDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: true
})

watch(initialValues, (newAsyncData) => {
    headerPersonalInfos.value.fullName = newAsyncData.fullname
    headerPersonalInfos.value.initials = getInitials(newAsyncData.fullname ?? '')
    savedValues.value = formatData()
    setValues(newAsyncData)
})

const onSubmit = handleSubmit(async (values) => {
    const hasChanged = <K extends keyof PatientDataSchema>(
        key: K,
        subKey?: keyof PatientDataSchema[K]
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

    const addressChanged =
        hasChanged('address', 'zipCode') ||
        hasChanged('address', 'country') ||
        hasChanged('address', 'state') ||
        hasChanged('address', 'city') ||
        hasChanged('address', 'street') ||
        hasChanged('address', 'number')

    const newData: Partial<Patient> = {
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
                  number: hasChanged('address', 'number') ? values.address.number : undefined
              }
            : undefined,
        email: hasChanged('email') ? values.email : undefined,
        phone: hasChanged('phone') ? values.phone : undefined
    }

    const isEmpty = Object.values(newData).every((value) => value === undefined)
    if (isEmpty) {
        isEditMode.value = false
        return
    }

    mutate(newData as any, {
        onSuccess: (newValue) => {
            if (newValue) {
                toast({ variant: 'success', description: 'Médico atualizado com sucesso! 🎉' })

                if (headerPersonalInfos.value) {
                    headerPersonalInfos.value.fullName =
                        newValue.first_name ?? headerPersonalInfos.value.fullName
                    headerPersonalInfos.value.initials = newValue.first_name
                        ? getInitials(newValue.first_name)
                        : headerPersonalInfos.value.initials
                    newValue?.first_name && getInitials(newValue.first_name)
                }

                queryClient.setQueryData(['patient-user', id], newValue)

                savedValues.value = formatData(newValue)
            }
        },
        onError: () => {
            toast({ variant: 'destructive', description: 'Erro ao atualizar o paciênte! 😢' })
        }
    })

    isEditMode.value = false
})

function handleCancel() {
    resetForm({
        values: savedValues.value
    })
    isEditMode.value = false
}

function handleDeleteUser() {
    deleteUserMutate(patientId, {
        onSuccess: () => {
            toast({
                variant: 'success',
                description: 'Paciênte removido com sucesso!'
            })
            router.push('/dashboard/pacientes')
        },
        onError: () => {
            toast({
                variant: 'destructive',
                description: 'Erro ao remover paciênte! 😢'
            })
        }
    })
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
                        <div class="text-sm text-gray-500">Paciente</div>
                    </div>
                </div>
            </div>

            <PersonalData :isEditMode="isEditMode" :isFieldDirty="isFieldDirty" />

            <div class="mt-6 space-x-2 flex justify-end">
                <template v-if="!isEditMode">
                    <DeleteUserDialog
                        :isPending="isPendingUser"
                        :onDelete="handleDeleteUser"
                        title="Você tem certeza que deseja remover esse paciênte?"
                        description="Esta ação não pode ser desfeita. Isso excluirá permanentemente o paciênte e
                    removerá seus dados de nossos servidores." />
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

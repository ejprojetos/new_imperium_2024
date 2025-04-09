<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Button } from '@/components/ui/button'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { type DoctorDataSchema } from './schema'
import { doctorDataSchema } from './schema'
import PersonalData from './form/personal-data.vue'
import ProfessionalData from './form/professional-data.vue'
import { useQuery, useMutation, QueryClient } from '@tanstack/vue-query'
import type { Doctor } from '@/types/users.types'
import { useRoute, useRouter } from 'vue-router'
import { fetcher } from '@/services/fetcher.service'
import { useToast } from '@/components/ui/toast/use-toast'
import { Loader } from 'lucide-vue-next'
import { useForm } from 'vee-validate'
import { getInitials } from '@/lib/utils'
import { useDeleteUserMutation } from '@/hooks/use-delete-user-mutation'

const { toast } = useToast()
const route = useRoute()
const router = useRouter()
const doctorId = route.params.id as string

const id = ref(doctorId)
const isEditMode = ref(false)
const doctorValid = ref(false)

const queryClient = new QueryClient()

const { data, isLoading, error } = useQuery({
    queryKey: ['doctor-user', id],
    queryFn: async () => await fetcher<Doctor>(`/users/${doctorId}`),
    staleTime: 5 * 1000
})

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo) => {
        return await fetcher<Doctor>(`/users/${doctorId}/`, {
            method: 'PATCH',
            body: JSON.stringify(newTodo)
        })
    }
})

const { mutate: deleteUserMutate, isPending: isPendingUser } = useDeleteUserMutation()

function formatData(raw: Doctor = data.value!) {
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
        specialty: raw.speciality,
        crm: raw.crm
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

const { isFieldDirty, handleSubmit, setValues, resetForm, values } = useForm<DoctorDataSchema>({
    validationSchema: doctorDataSchema,
    initialValues: initialValues.value ?? undefined,
    keepValuesOnUnmount: true
})

watch(data, () => {
    if (data.value?.roles[0].name !== 'DOCTOR') {
        router.push('/dashboard/medicos')

        return
    }

    doctorValid.value = true
})

watch(initialValues, (newAsyncData) => {
    headerPersonalInfos.value.fullName = newAsyncData.fullname
    headerPersonalInfos.value.initials = getInitials(newAsyncData.fullname ?? '')
    savedValues.value = formatData()
    setValues(newAsyncData)
})

function handleRemoveFile() {
    setValues({
        ...initialValues.value,
        file: undefined,
        attachDocument: null
    })
}

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
        hasChanged('address', 'number')

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
                  number: hasChanged('address', 'number') ? values.address.number : undefined
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

                queryClient.setQueryData(['doctor-user', id], newValue)

                savedValues.value = formatData(newValue)
            }
        },
        onError: () => {
            toast({ variant: 'destructive', description: 'Erro ao atualizar médico! 😢' })
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
    deleteUserMutate(doctorId, {
        onSuccess: () => {
            toast({
                variant: 'success',
                description: 'Médico removido com sucesso!'
            })
            router.push('/dashboard/recepcionistas')
        },
        onError: () => {
            toast({
                variant: 'destructive',
                description: 'Erro ao remover médico! 😢'
            })
        }
    })
}
</script>

<template>
    <LayoutDashboard>
        <UserNotFound v-if="error" navigateTo="/dashboard/medicos" />

        <div v-if="isLoading" class="flex justify-center items-center h-full">
            <Loader class="animate-spin text-gray-400" />
        </div>

        <form v-else-if="data && doctorValid" class="max-w-3xl mx-auto my-10" @submit="onSubmit">
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
                            {{ values.gender === 'Feminino' ? 'Dra.' : 'Dr.' }}
                            {{ headerPersonalInfos.fullName }}
                        </h2>
                        <div class="text-sm text-gray-500">
                            {{ values.gender === 'Feminino' ? 'Médica' : 'Médico' }}
                        </div>
                    </div>
                </div>
            </div>

            <Tabs default-value="personal">
                <TabsList
                    className="grid grid-cols-2 mb-4 border rounded-md p-1.5 border-gray-200 bg-white">
                    <TabsTrigger value="personal">Dados Pessoais</TabsTrigger>
                    <TabsTrigger value="work">Dados Profissionais</TabsTrigger>
                </TabsList>

                <TabsContent value="personal">
                    <PersonalData :isEditMode="isEditMode" :isFieldDirty="isFieldDirty" />
                </TabsContent>
                <TabsContent value="work">
                    <ProfessionalData
                        :onRemoveFile="handleRemoveFile"
                        :isEditMode="isEditMode"
                        :isFieldDirty="isFieldDirty"
                        :imageUrl="values.attachDocument" />
                </TabsContent>
            </Tabs>

            <div class="mt-6 space-x-2 flex justify-end">
                <template v-if="!isEditMode">
                    <DeleteUserDialog
                        :isPending="isPendingUser"
                        :onDelete="handleDeleteUser"
                        title="Você tem certeza que deseja remover?"
                        description="Esta ação não pode ser desfeita. Isso excluirá permanentemente o recepcionista e
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

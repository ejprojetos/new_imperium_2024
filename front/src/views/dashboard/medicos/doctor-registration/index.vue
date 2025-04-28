<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Loader } from 'lucide-vue-next'
import { useToast } from '@/components/ui/toast/use-toast'
import { Card, CardContent } from '@/components/ui/card'
import { useForm } from 'vee-validate'
import type { DoctorDataSchema } from './schema'
import { doctorDataSchema } from './schema'
import { PersonalData, AddressData, ContactData, ProfessionalData, SecurityData } from './form'
import { Button } from '@/components/ui/button'
import { useMutation } from '@tanstack/vue-query'
import { fetcher } from '@/services/fetcher.service'
import type { Doctor } from '@/types/users.types'
import { useRouter } from 'vue-router'

const { toast } = useToast()
const router = useRouter()

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo: {
        first_name: string
        cpf: string
        date_birth: string
        gender: string
        address: {
            zip_code: string
            country: string
            state: string
            city: string
            street: string
            number: string
            neighborhood: string
        }
        email: string
        phone: string
        crm: string
        password: string
    }) => {
        return await fetcher<Doctor>(`/users/`, {
            method: 'POST',
            body: JSON.stringify(newTodo)
        })
    }
})

const { isFieldDirty, handleSubmit, resetForm, setFieldError, resetField } =
    useForm<DoctorDataSchema>({
        validationSchema: doctorDataSchema
    })

function handleResetDocument() {
    resetField('file')
}

const onSubmit = handleSubmit(async (values: DoctorDataSchema) => {
    const formatDate = values.dateOfBirth.split('/')

    let base64Image: string | null = null

    if (values.file) {
        base64Image = await new Promise((resolve) => {
            const reader = new FileReader()
            reader.readAsDataURL(values.file as File)
            reader.onload = () => resolve(reader.result as string)
        })
    }

    const newData = {
        first_name: values.fullname,
        cpf: values.cpf,
        date_birth: `${formatDate[2]}-${formatDate[1]}-${formatDate[0]}`,
        gender: values.gender,
        roles: [
            {
                name: 'DOCTOR'
            }
        ],
        address: {
            zip_code: values.address.zipCode,
            country: values.address.country,
            state: values.address.state,
            city: values.address.city,
            street: values.address.street,
            number: values.address.number,
            neighborhood: values.address.neighborhood
        },
        formacao: values.formation,
        crm: values.crm,
        attach_document: base64Image,
        email: values.email,
        phone: values.phone,
        password: values.password
    }

    mutate(newData, {
        onSuccess() {
            toast({
                title: 'Sucesso',
                description: 'Médico cadastrado com sucesso!',
                variant: 'success'
            })

            resetForm()
            router.push('/dashboard/medicos')
        },
        onError(error: any) {
            if (error.status === 400) {
                toast({
                    title: 'Error',
                    description: 'Dados inválidos, verifique os dados',
                    variant: 'destructive'
                })

                Object.entries(error.errors).forEach(([field, errors]) => {
                    // @ts-ignore
                    setFieldError(field, errors[0] as string)
                })

                return
            }

            toast({
                title: 'Error',
                description: 'Error ao criar um médico, tente mais tarde',
                variant: 'destructive'
            })
        }
    })
})
</script>

<template>
    <LayoutDashboard>
        <div class="max-w-3xl mx-auto my-10">
            <div class="mb-8">
                <h1 class="text-3xl font-bold">Cadastrar Médico</h1>
                <p class="text-sm text-gray-500">
                    Preencha as informações abaixo para poder cadastrar um novo médico
                </p>
            </div>

            <form class="max-w-3xl mx-auto my-10" @submit="onSubmit">
                <Card>
                    <CardContent class="p-6 space-y-6">
                        <PersonalData :isFieldDirty="isFieldDirty" />
                        <AddressData :isFieldDirty="isFieldDirty" />
                        <ContactData :isFieldDirty="isFieldDirty" />
                        <ProfessionalData
                            :onResetDocumentImg="handleResetDocument"
                            :isFieldDirty="isFieldDirty" />
                        <SecurityData :isFieldDirty="isFieldDirty" />
                    </CardContent>
                </Card>
                <div class="mt-6 space-x-2 flex justify-end">
                    <Button type="submit">
                        <Loader v-if="isPending" class="animate-spin size-4 text-white" />
                        Cadastrar
                    </Button>
                </div>
            </form>
        </div>
    </LayoutDashboard>
</template>

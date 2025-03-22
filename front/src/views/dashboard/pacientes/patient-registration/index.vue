<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Loader } from 'lucide-vue-next'
import { useToast } from '@/components/ui/toast/use-toast'
import { Card, CardContent } from '@/components/ui/card'
import { useForm } from 'vee-validate'
import { Button } from '@/components/ui/button'
import { useMutation } from '@tanstack/vue-query'
import { fetcher } from '@/services/fetcher.service'
import { useRouter } from 'vue-router'
import { PersonalData, AddressData, ContactData, SecurityData } from './form'
import { patientDataSchema, type PatientDataSchema } from './schema'

const { toast } = useToast()
const router = useRouter()

const { isPending, mutate } = useMutation({
    mutationFn: async (newTodo: {
        first_name: string
        cpf: string
        date_birth: string
        roles: [
            {
                name: 'PATIENT'
            }
        ]
        gender: string
        address: {
            zip_code: string
            country: string
            state: string
            city: string
            street: string
            number: string
        }
        email: string
        phone: string
        password: string
    }) => {
        return await fetcher(`/users/`, {
            method: 'POST',
            body: JSON.stringify(newTodo)
        })
    }
})

const { isFieldDirty, handleSubmit, resetForm, setFieldError } = useForm<PatientDataSchema>({
    validationSchema: patientDataSchema
})

const onSubmit = handleSubmit(async (values) => {
    const formatDate = values.dateOfBirth.split('/')

    const newData = {
        first_name: values.fullname,
        cpf: values.cpf,
        date_birth: `${formatDate[2]}-${formatDate[1]}-${formatDate[0]}`,
        gender: values.gender,
        roles: [
            {
                name: 'PATIENT'
            }
        ] as [{ name: 'PATIENT' }],
        address: {
            zip_code: values.address.zipCode,
            country: values.address.country,
            state: values.address.state,
            city: values.address.city,
            street: values.address.street,
            number: values.address.number
        },
        email: values.email,
        phone: values.phone,
        password: values.password
    }

    mutate(newData, {
        onSuccess() {
            toast({
                title: 'Sucesso',
                description: 'Paciente cadastrado com sucesso!',
                variant: 'success'
            })

            resetForm()
            router.push('/dashboard/paciente')
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
                description: 'Error ao criar um paciente, tente mais tarde',
                variant: 'destructive'
            })
        }
    })
})
</script>

<template>
    <LayoutDashboard>
        <div class="max-w-3xl mx-auto my-10">
            <div className="mb-8">
                <h1 className="text-3xl font-bold">Cadastrar Pacient</h1>
                <p className="text-sm text-gray-500">
                    Preencha as informações abaixo para poder cadastrar um novo paciente
                </p>
            </div>

            <form class="max-w-3xl mx-auto my-10" @submit="onSubmit">
                <Card>
                    <CardContent class="p-6 space-y-6">
                        <PersonalData :isFieldDirty="isFieldDirty" />
                        <AddressData :isFieldDirty="isFieldDirty" />
                        <ContactData :isFieldDirty="isFieldDirty" />
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

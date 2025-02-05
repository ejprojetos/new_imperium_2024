<template>
    <LayoutDashboard>
        <div class="p-8 mx-auto w-full">
            <div class="">
                <h1 class="mb-6 text-[50px] font-normal">{{ FormData.fullName }}</h1>
            </div>
            <div class="pb-[70px] pt-[40px] px-[60px] mb-4 bg-white gap-x-4 w-[650px]">
                <section>
                    <h2 class="mb-4 text-xl font-bold text-black font-montserrat">
                        Dados Pessoais
                    </h2>

                    <div class="grid grid-cols-1 gap-4">
                        <div>
                            <label class="block mb-2 text-lg font-montserrat">Nome completo:</label>
                            <p class="px-2 py-1">{{ FormData.fullName }}</p>
                        </div>
                        <div class="flex gap-[80px]">
                            <div>
                                <label class="block mb-2 text-lg font-montserrat">
                                    Data de Nascimento:
                                </label>
                                <p class="px-2 py-1">{{ FormData.dateOfBirth }}</p>
                            </div>
                            <div>
                                <label class="block mb-2 text-lg font-montserrat">Gênero:</label>
                                <p class="px-2 py-1">{{ FormData.gener }}</p>
                            </div>
                        </div>
                        <div>
                            <label class="block mb-2 text-lg font-montserrat">CPF:</label>
                            <p class="px-2 py-1">{{ FormData.cpf }}</p>
                        </div>
                    </div>

                    <h2 class="mb-4 text-xl font-montserrat text-black mt-[30px] font-bold">
                        Endereço:
                    </h2>
                    <div class="flex gap-[40px]">
                        <div>
                            <label class="block mb-2 text-lg font-montserrat">País:</label>
                            <p class="px-2 py-1">{{ FormData.country }}</p>
                        </div>
                        <div>
                            <label class="block mb-2 text-lg font-montserrat">Estado:</label>
                            <p class="px-2 py-1">{{ FormData.state }}</p>
                        </div>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">Cidade:</label>
                        <p class="px-2 py-1">{{ FormData.city }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">Bairro:</label>
                        <p class="px-2 py-1">{{ FormData.neighborhood }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">CEP:</label>
                        <p class="px-2 py-1">{{ FormData.zipCode }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">
                            Logradouro:
                        </label>
                        <p class="px-2 py-1">{{ FormData.street }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">Número:</label>
                        <p class="px-2 py-1">{{ FormData.number }}</p>
                    </div>

                    <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">
                        Contato:
                    </h2>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">Email:</label>
                        <p class="px-2 py-1">{{ FormData.email }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">Celular:</label>
                        <p class="px-2 py-1">{{ FormData.phone }}</p>
                    </div>

                    <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">
                        Dados Profissionais:
                    </h2>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">
                            Formação:
                        </label>
                        <p class="px-2 py-1">{{ FormData.degree }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">
                            Especialidade:
                        </label>
                        <p class="px-2 py-1">{{ FormData.specialty }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">CRM:</label>
                        <p class="px-2 py-1">{{ FormData.crm }}</p>
                    </div>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">
                            Documentos comprobatórios:
                        </label>
                        <div class="px-2 py-1 text-white bg-blue-700 rounded-lg cursor-pointer">
                            <p class="w-full text-center text-white">{{ FormData.fileName }}</p>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { userService } from '@/services/users.service'
import type { User } from '@/types/users.types'

const route = useRoute()
const FormData = ref({
    fullName: '',
    dateOfBirth: '',
    gener: '',
    cpf: '',
    country: '',
    state: '',
    city: '',
    neighborhood: '',
    zipCode: '',
    street: '',
    number: '',
    email: '',
    phone: '',
    degree: '',
    specialty: '',
    crm: '',
    fileName: ''
})

const fetchDoctorData = async () => {
    try {
        const doctorId = route.params.id as string
        const data = (await userService.getUserById(doctorId)) as User

        FormData.value = {
            fullName: data.first_name || '',
            dateOfBirth: data.date_birth || '',
            gener: data.gender || '',
            cpf: data.cpf || '',
            country: data.address?.country || '',
            state: data.address?.state || '',
            city: data.address?.city || '',
            neighborhood: '', // Not available in API
            zipCode: data.address?.zip_code || '',
            street: data.address?.street || '',
            number: data.address?.number || '',
            email: data.email || '',
            phone: '', // Not available in API
            degree: data.formacao || '',
            specialty: data.roles?.find((role) => role.name === 'DOCTOR')?.name || '',
            crm: data.crm || '',
            fileName: data.attach_document || ''
        }
    } catch (error) {
        console.error('Error fetching doctor data:', error)
    }
}

onMounted(() => {
    fetchDoctorData()
})
</script>

<style scoped>
h1,
h2,
p,
span,
label {
    font-family: 'montserrat';
}

label {
    color: #010424;
    font-weight: 600;
}
</style>

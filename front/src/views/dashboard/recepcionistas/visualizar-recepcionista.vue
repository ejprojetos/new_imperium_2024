<template>
    <LayoutDashboard>
        <div class="p-8">
            <div class="">
                <h1 class="mb-6 text-[50px] font-normal">{{ FormData.name }}</h1>
            </div>
            <div class="pb-[70px] pt-[40px] px-[60px] mb-4 bg-white gap-x-4 w-[650px]">
                <section>
                    <h2 class="mb-4 text-xl font-bold text-black font-montserrat">
                        Dados Pessoais
                    </h2>

                    <div class="grid grid-cols-1 gap-4">
                        <div>
                            <label class="block mb-2 text-lg font-montserrat">Nome:</label>
                            <p class="px-2 py-1">{{ FormData.name }}</p>
                        </div>
                        <div>
                            <label class="block mb-2 text-lg font-montserrat">Sobrenome:</label>
                            <p class="px-2 py-1">{{ FormData.lastName }}</p>
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

                    <!-- Continue with similar pattern for other fields -->

                    <h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">
                        Expediente:
                    </h2>
                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">
                            Dias de Trabalho:
                        </label>
                        <div class="flex flex-wrap gap-2">
                            <span
                                v-for="(day, index) in weekDays"
                                :key="index"
                                :class="[
                                    'px-px-4 py-2 rounded-2xl w-[90px] h-[30px] flex items-center justify-center font-montserrat',
                                    selectedDays.includes(day)
                                        ? 'bg-[#00428F] text-white'
                                        : 'bg-[#DEECFA] text-gray-700'
                                ]">
                                {{ day }}
                            </span>
                        </div>
                    </div>

                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">Turnos:</label>
                        <div class="flex flex-wrap gap-2">
                            <span
                                v-for="(shift, index) in shifts"
                                :key="index"
                                :class="[
                                    'px-px-4 py-2 rounded-2xl w-[90px] h-[30px] flex items-center justify-center font-montserrat',
                                    selectedShifts.includes(shift)
                                        ? 'bg-[#00428F] text-white'
                                        : 'bg-[#DEECFA] text-gray-700'
                                ]">
                                {{ shift }}
                            </span>
                        </div>
                    </div>

                    <div>
                        <label class="block mt-[20px] mb-2 text-lg font-montserrat">
                            Disponibilidade para plantões:
                        </label>
                        <p class="px-2 py-1">{{ FormData.plantoes === 'sim' ? 'Sim' : 'Não' }}</p>
                    </div>
                </section>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { ref } from 'vue'

const weekDays = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
const shifts = ['Matutino', 'Vespertino', 'Noturno']

const selectedDays = ref<string[]>(['Segunda', 'Quarta', 'Sexta']) // Example data
const selectedShifts = ref<string[]>(['Matutino', 'Vespertino']) // Example data

// Example data - in real application, this would come from props or API
const FormData = ref({
    name: 'João',
    lastName: 'Silva',
    dateOfBirth: '1990-01-01',
    gener: 'Masculino',
    cpf: '123.456.789-00',
    country: 'Brasil',
    state: 'RN',
    city: 'Natal',
    neighborhood: 'Centro',
    zipCode: '59000-000',
    street: 'Rua Principal',
    number: '123',
    email: 'joao.silva@email.com',
    phone: '(84) 99999-9999',
    plantoes: 'sim'
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

p {
    color: #333;
}
</style>

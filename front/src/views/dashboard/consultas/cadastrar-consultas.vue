<template>
    <LayoutDashboard>
        <div class="grid grid-cols-1 gap-4 px-12 mt-12">
            <router-link to="/dashboard/medicos">
                <h2
                    class="text-xl font-semibold text-gray-600 transition duration-300 ease-in-out hover:text-gray-800">
                    Voltar
                </h2>
            </router-link>

            <h1 class="mx-auto w-1/2 titulo-cadastro max-lg:w-full">Cadastrar Consultas</h1>
            <div class="w-full bg-white rounded-lg shadow-lg max-w-[1000px] mx-auto p-10">
                <div class="grid grid-cols-1 gap-4">
                    <div>
                        <label for="fullName" class="block mb-1 font-semibold titulo-label">
                            Nome do Paciente:
                        </label>
                        <select
                            class="w-full select select-bordered texto-opcoes"
                            v-model="optionSelected.fullName">
                            <option v-for="option in formData.fullName" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="consultation" class="block mb-1 font-semibold titulo-label">
                            Consulta:
                        </label>
                        <input
                            type="text"
                            class="w-full rounded-full input input-bordered texto-opcoes"
                            v-model="optionSelected.consultation" />
                    </div>
                    <div>
                        <label for="specialty" class="block mb-1 font-semibold titulo-label">
                            Especialidade:
                        </label>
                        <select
                            class="w-full select select-bordered texto-opcoes"
                            v-model="optionSelected.specialty">
                            <option v-for="option in formData.specialty" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="medicName" class="block mb-1 font-semibold titulo-label">
                            Médico:
                        </label>
                        <select
                            class="w-full select select-bordered texto-opcoes"
                            v-model="optionSelected.medicName">
                            <option value="" disabled>Selecione um médico</option>
                            <option v-for="doctor in doctors" :key="doctor.id" :value="doctor.id">
                                Dr(a). {{ doctor.first_name }} {{ doctor.last_name }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label for="room" class="block mb-1 font-semibold titulo-label">
                            Local:
                        </label>
                        <select
                            class="w-full select select-bordered texto-opcoes"
                            v-model="optionSelected.room">
                            <option v-for="option in formData.room" :key="option">
                                {{ option }}
                            </option>
                        </select>
                    </div>
                    <div class="grid grid-cols-1 gap-1">
                        <label class="block mb-1 font-semibold">Motivo da consulta:</label>
                        <input
                            type="text"
                            placeholder="Digite o motivo da consulta"
                            class="w-full rounded-full input input-bordered texto-opcoes"
                            v-model="motivo" />
                    </div>
                    <div class="grid grid-cols-2 gap-1">
                        <div class="grid grid-cols-1 gap-1">
                            <label for="dateInput" class="block mb-1 font-semibold">
                                Selecione uma data:
                            </label>
                            <input
                                type="date"
                                id="dateInput"
                                v-model="selectedDate"
                                class="w-3/6 rounded-full input input-bordered input-group" />
                        </div>
                        <div class="grid grid-cols-1 gap-1">
                            <label for="timeInput" class="block mb-1 font-semibold">
                                Selecione uma hora:
                            </label>
                            <input
                                type="time"
                                id="timeInput"
                                v-model="selectedTime"
                                class="px-5 w-2/5 rounded-full input input-bordered input-group" />
                        </div>
                    </div>
                    <div class="flex gap-x-2">
                        <label for="timeInput" class="block mb-1 font-semibold">Fila:</label>
                        <label for="">1º</label>
                    </div>
                    <button
                        class="p-1 w-1/6 text-white btn btn-active btn-neutral hover:bg-blue"
                        style="background-color: #00428f"
                        @click.prevent="handleSubmit"
                        :disabled="isSubmitting">
                        {{ isSubmitting ? 'Cadastrando...' : 'Cadastrar' }}
                    </button>

                    <dialog id="my_modal_2" class="modal">
                        <div class="grid grid-cols-1 gap-4 modal-box">
                            <h3 class="text-lg font-bold titulo-modal">
                                Consulta cadastrada com sucesso!
                            </h3>

                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold">{{ labels.fullName }}:</label>
                                <label>{{ optionSelected.fullName }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold">
                                    {{ labels.consultation }}:
                                </label>
                                <label>{{ optionSelected.consultation }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold">{{ labels.specialty }}:</label>
                                <label>{{ optionSelected.specialty }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold">{{ labels.medicName }}:</label>
                                <label>{{ optionSelected.medicName }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold">{{ labels.room }}:</label>
                                <label>{{ optionSelected.room }}</label>
                            </div>
                            <div class="grid grid-cols-1">
                                <label for="" class="font-semibold">{{ labels.reason }}:</label>
                                <label>{{ motivo }}</label>
                            </div>
                            <div class="grid grid-cols-2">
                                <div class="grid grid-cols-1">
                                    <label for="" class="font-semibold">{{ labels.date }}:</label>
                                    <label>{{ formattedDate }}</label>
                                </div>
                                <div class="grid grid-cols-1">
                                    <label for="" class="font-semibold">{{ labels.time }}:</label>
                                    <label>{{ selectedTime }}</label>
                                </div>
                            </div>
                            <div class="grid grid-cols-1"></div>

                            <label for="timeInput" class="block mb-1 font-semibold">Fila: 1º</label>

                            <button
                                class="w-1/6 text-white btn btn-active btn-neutral hover:bg-blue"
                                style="background-color: #00428f"
                                onclick="my_modal_2.close()">
                                Fechar
                            </button>
                        </div>
                        <form method="dialog" class="modal-backdrop">
                            <button>close</button>
                        </form>
                    </dialog>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { ref, reactive, computed, onMounted } from 'vue'
import { useAppointmentStore } from '@/stores/appointments/appointments.store'
import type { Appointment } from '@/types/appointments.types'
import { useRouter } from 'vue-router'
import { toast } from 'vue-sonner'
import { storeToRefs } from 'pinia'
import { useUserStore } from '@/stores/users/users.store'

const userStore = useUserStore()
const { doctors } = storeToRefs(userStore)

const router = useRouter()
const appointmentStore = useAppointmentStore()

const selectedTime = ref('')
const motivo = ref('')
const optionSelected = reactive({
    fullName: '',
    consultation: '',
    specialty: '',
    medicName: '',
    room: ''
})

const appointmentForm = reactive<Partial<Appointment>>({
    patient: 0,
    doctor: 0,
    clinic: 1,
    appointment_date: '',
    reason: '',
    room: 0
})

const formattedDate = computed(() => {
    if (!selectedDate.value) return ''
    return new Date(selectedDate.value).toLocaleDateString()
})

const validateForm = () => {
    if (!optionSelected.fullName) throw new Error('Selecione um paciente')
    if (!optionSelected.medicName) throw new Error('Selecione um médico')
    if (!optionSelected.room) throw new Error('Selecione uma sala')
    if (!selectedDate.value) throw new Error('Selecione uma data')
    if (!selectedTime.value) throw new Error('Selecione um horário')
    if (!motivo.value) throw new Error('Digite o motivo da consulta')
}

const formData = reactive({
    profileImage: '../../../assets/placeholder.png',
    fullName: ['Gabriele Rocha de Carvalho', 'Rômulo Deyvid', 'Han Solo', 'Greedo'],
    consultation: ['1ª Consulta', 'Retorno'],
    specialty: ['Oftalmologia', 'Cardiologia', 'Urologia'],
    room: ['Sala 01', 'Sala 02', 'Sala 03'],
    birthDate: '10/10/1981',
    gender: 'Feminino',
    cpf: '999.999.999-99',
    country: 'Brasil',
    state: 'RN',
    city: 'Parnamirim',
    neighborhood: 'Nova Parnamirim',
    zipCode: '00000-000',
    street: 'Av. Ayrton Senna',
    number: '000',
    email: 'exemplo99@hotmail.com',
    phone: '(00) 00000-0000',
    allergies: '',
    recurringProblems: '',
    medication: ''
})

const isSubmitting = ref(false)
const formError = ref<string | null>(null)

const labels = {
    fullName: 'Nome do Paciente',
    consultation: 'Consulta',
    specialty: 'Especialidade',
    medicName: 'Nome do médico',
    reason: 'Motivo da consulta',
    date: 'Data da Consulta',
    time: 'Hora da Consulta',
    room: 'Local',
    gender: 'Gênero',
    cpf: 'CPF',
    country: 'País',
    state: 'Estado',
    city: 'Cidade',
    neighborhood: 'Bairro',
    zipCode: 'CEP',
    street: 'Logradouro',
    number: 'Número',
    email: 'Email',
    phone: 'Celular'
}
const selectedDate = ref(null)

const handleSubmit = async () => {
    try {
        isSubmitting.value = true

        // Validate form
        validateForm()

        const appointmentData = formatAppointmentData()

        await appointmentStore.createAppointment(appointmentData)

        toast.success('Consulta cadastrada com sucesso!')

        const modal = document.getElementById('my_modal_2') as HTMLDialogElement
        modal.showModal()

        setTimeout(() => {
            router.push('/dashboard/consultas')
        }, 2000)
    } catch (error) {
        if (error instanceof Error) {
            toast.error(error.message)
        } else {
            toast.error('Erro ao cadastrar consulta')
        }
        console.error(error)
    } finally {
        isSubmitting.value = false
    }
}

const formatAppointmentData = (): Partial<Appointment> => {
    const dateTime = new Date(`${selectedDate.value}T${selectedTime.value}`)
    return {
        patient: parseInt(optionSelected.fullName) || 0,
        doctor: parseInt(optionSelected.medicName),
        clinic: 1,
        appointment_date: dateTime.toISOString(),
        reason: motivo.value,
        room: parseInt(optionSelected.room) || 0,
        status: 'scheduled'
    }
}

onMounted(() => {
    userStore.fetchDoctors()
})
</script>

<style scoped>
select {
    border-radius: 50px;
    width: 100%;
}

.titulo-modal {
    color: #010424;
    font-family: Montserrat;
    font-size: 30px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.titulo-cadastro {
    color: #010424;
    font-family: Montserrat;
    font-size: 50px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.titulo-label {
    color: #010424;
    font-family: Montserrat;
    font-size: 20px;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
}

.texto-opcoes {
    color: #010424;
    font-family: Montserrat;
    font-size: 18px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

input::placeholder {
    color: #010424;
    font-family: Montserrat;
    font-size: 18px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

.input-group {
    height: 2rem;
}

.modal-box {
    max-width: 40rem;
}
</style>
